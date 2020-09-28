'''import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('pramodmittaltech@gmail.com','mittal@12345')
message = "sending a message"
server.sendmail('pramodmittaltech@gmail.com','p.mittal8006@gmail.com',message)
print('message has been sent!!!!!!')
server.quit()'''

#2nd way

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
msg = MIMEMultipart()
from email import encoders

def send(filename):
    from_add = "pramodmittaltech@gmail.com"
    to_add = "p.mittal8006@gmail.com"
    subject = "Finance Stock Report"
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject
    body = "<b>Today's Finance Stock Report Attached!</b>"
    msg.attach(MIMEText(body,'html'))

    #attaching csv file
    my_file = open(filename,'rb')    #binary mode
    part = MIMEBase('application','octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment;filename =  ' +  filename)
    msg.attach(part)
    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_add,'blablafake')
    server.sendmail(from_add,to_add,message)
    print('message has been sent!!!!')
    server.quit()