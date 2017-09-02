import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

username = 'testedboy@gmail.com'
password = 'soothingair'


class MessengerClass:

    def __init__(self, source, destination, subject, message):
        self.source = source
        self.destination = destination
        self.subject = subject
        self.message = message
        try:
            self.email_server = smtplib.SMTP('smtp.gmail.com:587')
        except Exception as e:
            print('Cloud not connect to smpt server before sending a mail' +
                  str(e))

    def send_email_notification(self):
        try:
            multipartmsg = MIMEMultipart()
            multipartmsg['From'] = self.source
            multipartmsg['TO'] = self.destination
            multipartmsg['Subject'] = self.subject
            multipartmsg.attach(MIMEText(self.message))
            # Establishing connection to the server
            self.email_server.ehlo()
            # User TLS for encrypted data transfer
            self.email_server.starttls()
            self.email_server.ehlo()
            self.email_server.login(username, password)
            # Send mail
            self.email_server.sendmail(self.source, self.destination,
                                       multipartmsg.as_string())
        except Exception as e:
            print('Exception found while sending email from %s ,to '
                  ' %s subject %s message %s ' % (self.source,
                                                  self.destination,
                                                  self.subject,
                                                  self.message) + str(e))


if __name__ == '__main__':
    messenger_instance = MessengerClass('testedboy@gmail.com',
                                        'testedboy@gmail.com',
                                        'Test',
                                        'Hello')
    messenger_instance.send_email_notification()
