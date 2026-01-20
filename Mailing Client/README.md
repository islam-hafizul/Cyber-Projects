# Mailing Client - Python Email Automation

A Python script to send emails with attachments using Gmail's SMTP server. 
- Send emails with plain text body
- Attach files (images, documents, etc.)
- Secure connection using SSL
- Easy configuration

## Quick Start
### Prerequisites
- Python 2.7+
- Gmail account with [App Password](https://myaccount.google.com/apppasswords) enabled

### Installation
1. Clone or download the script
2. Install no additional packages (uses Python's built-in modules)

### Configuration
1. Enable 2-Step Verification in your Google Account
2. Generate an App Password for "Mail"
3. Update the script with your email details

### Usage
1. Place your message in `message.txt`
2. Place attachment file (e.g., `image.jpg`) in same directory
3. Run the script: `python email_sender.py` 
4. Enter your Gmail App Password when prompted

## License
Free to use and modify.

## Support
For issues, check Google's [App Passwords guide](https://support.google.com/accounts/answer/185833)
