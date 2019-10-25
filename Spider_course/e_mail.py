import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header   
import os
 
class email:
    def __init__(self,username,password,sender,receiver):
        self.username = username
        self.password = password
        self.sender = sender
        self.receiver = receiver
        self.send_img()
        self.smtp()
        os.remove("course.png")

    def smtp(self):
        try:
            smtp = smtplib.SMTP() 
            smtp.connect("smtp.qq.com", 25)
            smtp.login(self.username,self.password)  
            smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
            print ("邮件发送成功")
            smtp.quit()
        except smtplib.SMTPException as e:
            print(e)
            smtp.quit()

    def send_img(self):
        self.msg = MIMEMultipart('related')
        self.msg['Subject'] = Header('course','utf-8')
        self.msg['From'] = Header(self.sender,'utf-8')
        self.msg['To'] = Header(self.receiver,'utf-8')
        
        mail_msg = "<p><img src='cid:image'></p>"
        self.msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))
        
        Image = MIMEImage(open('course.png','rb').read())
        Image.add_header('Content-ID', 'image')
        self.msg.attach(Image)
        
        
        
   


