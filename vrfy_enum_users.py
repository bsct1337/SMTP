import socket
import argparse


def vrfy_email(email, smtp_server='localhost'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((smtp_server, 25))
    banner = s.recv(1024).decode()
    # print(f"[+] Connected to {smtp_server}: {banner}")

    s.send(b'VRFY ' + email.encode() + b'\r\n')
    result = s.recv(1024).decode()
    if result[:3] == '250':
        print(f"[+] {email} exists")
        s.close()
        return True
    else:
        print(f"[-] {email} does not exist")
        s.close()
        return False


parser = argparse.ArgumentParser(description='SMTP VRFY Email Verifier')
parser.add_argument('wordlist', help='File containing a list of email addresses to verify')
parser.add_argument('--server', help='SMTP server to connect to (default: localhost)', default='localhost')
args = parser.parse_args()

with open(args.wordlist, 'r') as f:
    email_list = f.read().splitlines()

for email in email_list:
    vrfy_email(email, args.server)
