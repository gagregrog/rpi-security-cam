import smtplib
from os import environ
from time import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from utility import info

class Emailer():
    def __init__(self, email_debounce=60):
        self.username = environ['GMAIL_USER']
        self.pw = environ['GMAIL_PW']
        recipients = environ.get('RECIPIENTS') or self.username
        self.recipients = recipients.split(' ')
        self.last_email_at = None
        self.email_debounce = email_debounce

    
    def login(self):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(self.username, self.pw)
        self.server = server

    
    def logout(self):
        self.server.close()
        self.server = None


    def send_email(self, subject='Person Detected', body='__PERSON_DETECTED__', filename=None):
        now = time()

        if self.last_email_at is None or (now - self.last_email_at > self.email_debounce):
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(self.recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            if filename:
                attachment = open(filename, 'rb')
                p = MIMEBase('application', 'octet-stream')
                p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', 'attachment; filename={}'.format(filename))
                msg.attach(p)

            self.last_email_at = now
            self.login()
            email_text = msg.as_string()
            self.server.sendmail(self.username, self.recipients, email_text)
            self.logout()

            info('__EMAIL_SENT__')
