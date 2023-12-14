import re
import time
import paramiko
import random
import yagmail


SSH_SERVER_IP = "IP_ADDRESS"
SSH_USERNAME = "USERNAME"
SSH_PASSWORD = "PASSWORD"
GMAIL_USERNAME = 'GMAIL_USERNAME'
GMAIL_PASSWORD = 'GMAIL_PASSWORD'
KEYWORDS_REGEX = re.compile(r'sorry|help|wrong|Cant Access|Did it again|not working|no control|Database down|down|crashed', re.IGNORECASE)
yagmail.register(GMAIL_USERNAME, GMAIL_PASSWORD)
bs1 = ["server", "Network", "Windows syslog", "linux compatiablity", "office Mangement Software", "Teams Mangement Software", "Cisco", "WebServer", "Firewall", "Network Hub", "Slack Domain Controler", "Linux print spooler", "Windows encryption matrix", "Mac database indexer", "Apple pie standerdising volly", "Linux visualisation launch software", "Ubuntu time displacement controler", "Redhat security network", "Fedora At Tipper controler", "Arch'er control bow", "Backtrack dragon parrot instance"]
bs2 = ["corrupted its kernal", "become outdated", "crashed", "been hacked", "had a power loss", "become flood by UDP traffic", "become corrupted by the SDR", "had API failure", "adobe reader overflow"]
bs3 = ["fixing", "securing", "restarting", "replacing", "upgrading", "downgrading" "Installing new software to", "reinstalling", "reconfiguring", "rebooting", "rebooting the server", "rebooting the network", "rebooting the firewall", "rebooting the webserver", "rebooting the domain controler", "rebooting the slack domain controler", "rebooting the office management software", "rebooting the teams management software", "rebooting the cisco", "rebooting the network hub", "rebooting the linux compatiablity", "rebooting the windows syslog", "rebooting the server"]

while True:
    try:
        mail = yagmail.SMTP(GMAIL_USERNAME, GMAIL_PASSWORD)
        for email in mail.inbox().mail(subject=KEYWORDS_REGEX):
            sender = email.sender
            subject = "RP " + email.subject
            body = email.body
            REPLY_BODY = (
                "The " + random.choice(bs1) + " has " + random.choice(bs2) +
                " and I am " + random.choice(bs3) +
                " It now, and should be up soon, give it like 10 minutes"
            )

            mail.send(sender, subject, REPLY_BODY)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(SSH_SERVER_IP, username=SSH_USERNAME, password=SSH_PASSWORD)
            ssh.exec_command("reboot")
            ssh.close()
            timedate = time.strftime("%Y-%m-%d %H:%M:%S")
            print("Fucking " + sender + " broke the system...again at " + timedate)
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        mail.close()
        time.sleep(1300)
