import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "hatamiarash7@gmail.com"
toaddr = "hatamiarash7@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Arash's Message"
 
body = "Hello"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Mna32#%12Thp")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()