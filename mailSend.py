import smtplib
import ssl
from email.mime.text import MIMEText
from credentials import *  

port=465 #server port for SSL
smtp='smtp.strato.de' #SMTP Server

subject='Testbetreff'
text='Testnachricht'

message=MIMEText(text, 'plain')
message['Subject']=subject
message['From']=sender_email
message['To']=receiver_email

with smtplib.SMTP_SSL(smtp, port, context=ssl.create_default_context()) as server:
    server.login(user,password)
    server.sendmail(sender_email, receiver_email, message.as_string())
