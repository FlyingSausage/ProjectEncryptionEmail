import smtplib
from email.mime.text import MIMEText
from email.header import Header

class mymail:
    def __init__(self,sender:str, reciever:str, message:str,Subject:str,From:str) -> None:
        self.sender = sender
        self.receiver = reciever
        self.message = message
        self.Subject = Subject
        self.From = From
    
    def dispMsg(self):
        print(self.message)

    def sendMail(self):
        #login to Email
        service = input('please enter your email service smtp url, such as smtp.gmail.com: ')
        port = input('please enter the port of your smtp service: ')
        smtp_obj = smtplib.SMTP_SSL(service,port) #port for my gmail is 465
        uname = self.sender
        upasswd = input('please enter your email password: ')
        smtp_obj.login(uname,upasswd)
        #Convert str messages to email elements
        msg = self.message
        msg_body = MIMEText(msg,'plain','utf-8')
        msg_body['Subject'] = Header(self.Subject,'utf-8')
        msg_body['From'] = Header(self.From,'utf-8')

        #send
        smtp_obj.sendmail(uname,[self.receiver],msg_body.as_string())
        print('Message Sent')