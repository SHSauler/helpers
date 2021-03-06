from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

SENDER = "steffen.sauler@"
FROM = ""
MAILSERVER = "mail.server.com"
MSG_PRIORITY = '3'

def sendmail(recipients, inp_msg, inp_subject, msg_priority=MSG_PRIORITY):
    """ Sends HTML mails """

    msg = MIMEMultipart('alternative')
    msg['Subject'] = inp_subject
    msg['From'] = FROM
    
    if isinstance(recipients, str):
        msg['To'] = "{0}".format(recipients)
    else:
        msg['To'] = ", ".join(recipients)
    
    msg["X-Priority"] = msg_priority

    part1 = MIMEText("Message is HTML", "plaintext")
    part2 = MIMEText(inp_msg, 'html')

    msg.attach(part1)
    msg.attach(part2)

    smtp_message = smtplib.SMTP(MAILSERVER)
    smtp_message.sendmail(SENDER, recipients, msg.as_string())
