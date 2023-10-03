import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

host = "smtp.gmail.com"
port = 465
username = "connord79@gmail.com"

From = "connord79@gmail.com"
To = "connord79@gmail.com"


def SendMail(ImgFileName, description):
    with open(ImgFileName, 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'NASA image of the day'
    msg['From'] = 'connord79@gmail.com'
    msg['To'] = 'connord79@gmail.com'

    text = MIMEText(description)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename("image.jpg"))
    msg.attach(image)

    context = ssl.create_default_context()
    s = smtplib.SMTP_SSL(host, port, context=context)
    #s = smtplib.SMTP(host, port)
    s.login(username, password)
    s.sendmail(From, To, msg.as_string())
    s.quit()