import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_mail = 'my@gmail.com'
password = input('Type credentials of your mail: ')
to_mail = 'your@gmail.com'
subject = 'Test Email with Attachment'
with open('message.txt') as f: # keep the file in the same directory
    body = f.read()

msg = MIMEMultipart()
msg['From'] = from_mail
msg['To'] = to_mail
msg['Subject'] = subject
msg['Bcc'] = to_mail
msg.attach(MIMEText(body, 'plain'))

filename = 'image.jpg'
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename={filename}')

msg.attach(part)
text = msg.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_mail, password)
    server.sendmail(from_mail, to_mail, text)
