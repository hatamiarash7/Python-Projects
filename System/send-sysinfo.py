import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import platform
 

info = platform.uname()
platform_type = str(info[0])
system_name = str(info[1])
platform_name = str(info[2])
platform_version = str(info[3])
machine_type = str(info[4])
machine_info = str(info[5])

fromaddr = "hatamiarash7@gmail.com"
toaddr = "hatamiarash7@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Arash's Message"
 
body = "Your System Info :\n   " + platform_type + " " + platform_name + " - " + platform_version + "\n   " + machine_type + "\n   " + machine_info
body = body + "\n\nSystem Name : " + system_name
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Mna32#%12Thp")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()