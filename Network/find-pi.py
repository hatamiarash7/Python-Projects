import os, string, re, sys, time, thread
import subprocess

def main():
	ip = find_ip()
	print("You Raspberry Pi's IP : " + ip)
	print("Connecting ...\n")
	cmd = "ssh pi@" + ip
	subprocess.call(cmd, shell=True)
	
def find_ip():
    cmd = "nmap -sn 192.168.1.0/24"
    res = invoke(cmd)
    ip = None
    lines = res.split('\n')
    for i in lines:
        #find ip address
        m = find('(Pi.*)', i)
        if m: ip = find('(192.*)', lines[lines.index(i)-2])
    if ip:
         return ip
        
def find(needle, haystack):
    try:
        match = re.search(needle, haystack)
        if len(match.groups()) > 1:
            return match.groups()
        else: 
            return match.groups()[0]
    except: pass

def invoke(cmd):
    (sin, sout) = os.popen2(cmd)
    return sout.read()

if __name__ == "__main__":
    main()
