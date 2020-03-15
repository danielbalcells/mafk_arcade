import smtplib


HOST = 'smtp.gmail.com'
PORT = 465 
FROM_ADDR = 'your@email.com'
PASSWORD = 'password'


class Mailer(object):

    def __init__(self, subject):
        self.server = self.init_server()
        self.subject = subject
        self.from_addr = FROM_ADDR

    def init_server(self):
        server = smtplib.SMTP_SSL(HOST, PORT)
        server.ehlo()
        server.login(FROM_ADDR, PASSWORD)
        return server

    def send(self, dest_addr, message):
        message = f"Subject: {self.subject}\n\n" + message
        self.server.sendmail(self.from_addr, dest_addr, message)
