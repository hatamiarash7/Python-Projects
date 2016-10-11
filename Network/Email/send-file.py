import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "hatamiarash7@gmail.com"
toaddr = "hatamiarash7@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Arash's File"
 
body = "Hello"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "send-text.py"
attachment = open("send-text.py", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Mna32#%12Thp")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()