import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'PostmanBot'
email['to'] = 'dummy@dummy.com'
email['subject'] = 'Hello!'

email.set_content(html.substitute({'name': 'Friend'}), 'html')

def send_email():
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('dummy@dummy.com','mypassword')
        smtp.send_message(email)
        print('Email sent!')

send_email()