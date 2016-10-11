import os
import socket
import smtplib
from requests import get
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


if os.name != "nt":
    import fcntl
    import struct
    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

def get_internal_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

def get_external_ip():
    ip = get('https://api.ipify.org').text
    return ip

fromaddr = "hatamiarash7@gmail.com"
toaddr = "hatamiarash7@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Your System's IPs"

internal_ip = get_internal_ip()
external_ip = get_external_ip()
body = "Internal IP Address : " + str(internal_ip) + "\nExternal IP Address : " + str(external_ip)
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Mna32#%12Thp")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

