import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '<your real name>'
email['to'] = '<another email address>'
email['subject'] = '<email subject>'

email.set_content((html.substitute(name='<$name in html file>')), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<your gmail account>', '<your gmail password>')
    smtp.send_message(email)
    print('All done!')