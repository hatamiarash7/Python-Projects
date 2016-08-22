import base64
import getpass
import os
import socket
import sys
import traceback
from paramiko.py3compat import input
import paramiko
from colorama import Fore, Back, Style
import colorama
try:
    import interactive
except ImportError:
    from . import interactive
colorama.init()
def ascii_art():
    print
    print(Fore.CYAN + ' + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +')
    print(Fore.CYAN + ' +' + Fore.YELLOW + "                               _       _    _         _                      _   " + Fore.CYAN + '+')
    print(Fore.CYAN + ' +' + Fore.YELLOW + "      /\                      | |     | |  | |       | |                    (_)  " + Fore.CYAN + '+')
    print(Fore.CYAN + ' +' + Fore.YELLOW + "     /  \    _ __   __ _  ___ | |__   | |__| |  __ _ | |_   __ _  _ __ ___   _   " + Fore.CYAN + '+')
    print(Fore.CYAN + ' +' + Fore.YELLOW + "    / /\ \  | '__| / _` |/ __|| '_ \  |  __  | / _` || __| / _` || '_ ` _ \ | |  " + Fore.CYAN + '+')
    print(Fore.CYAN + ' +' + Fore.YELLOW + "   / ____ \ | |   | (_| |\__ \| | | | | |  | || (_| || |_ | (_| || | | | | || |  " + Fore.CYAN + '+')
    print(Fore.CYAN + ' +' + Fore.YELLOW + "  /_/    \_\|_|    \__,_||___/|_| |_| |_|  |_| \__,_| \__| \__,_||_| |_| |_||_|  " + Fore.CYAN + '+')
    print(Fore.CYAN + ' +                                                                                 ' + Fore.CYAN + '+')
    print(Fore.CYAN + ' + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +' + Style.RESET_ALL)
    print
# setup logging
paramiko.util.log_to_file('ssh.log')
# Paramiko client configuration
UseGSSAPI = True             # enable GSS-API / SSPI authentication
DoGSSAPIKeyExchange = True
port = 22

ascii_art()

# get hostname
username = ''
if len(sys.argv) > 1:
    hostname = sys.argv[1]
    if hostname.find('@') >= 0:
        username, hostname = hostname.split('@')
else:
    hostname = input('Enter Host : ')
if len(hostname) == 0:
    print('### Hostname/IP required !')
    sys.exit(1)

if hostname.find(':') >= 0:
    hostname, portstr = hostname.split(':')
    port = int(portstr)


# get username
if username == '':
    username = input('Enter Username : ')
    if len(username) == 0:
        print('### Username required !')
        sys.exit(1)
if not UseGSSAPI or (not UseGSSAPI and not DoGSSAPIKeyExchange):
    password = getpass.getpass('Enter Password For %s@%s : ' % (username, hostname))

# now, connect and use paramiko Client to negotiate SSH2 across the connection
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    print('### Connecting ...')
    if not UseGSSAPI or (not UseGSSAPI and not DoGSSAPIKeyExchange):
        client.connect(hostname, port, username, password)
    else:
        # SSPI works only with the FQDN of the target host
        hostname = socket.getfqdn(hostname)
        try:
            client.connect(hostname, port, username, gss_auth=UseGSSAPI,
                           gss_kex=DoGSSAPIKeyExchange)
        except Exception:
            password = getpass.getpass('Password for %s@%s: ' % (username, hostname))
            client.connect(hostname, port, username, password)
    chan = client.invoke_shell()
    print(repr(client.get_transport()))
    print('### Here we go!\n')
    interactive.interactive_shell(chan)
    chan.close()
    client.close()

except Exception as e:
    print('### Caught exception: %s: %s' % (e.__class__, e))
    traceback.print_exc()
    try:
        client.close()
    except:
        pass

sys.exit(1)
