#!/usr/bin/env python3

"""
Retrieve messages from IMAP mailbox
"""
import imaplib

############################## Settings #######################################

EMAIL_ACCOUNT = ""
MAILBOX = 'INBOX'
SERVER = ""
PASS = ""

############################## /Settings ######################################


Mailbox = imaplib.IMAP4_SSL(SERVER)

# Authentication
try:
    returnval, data = Mailbox.login(EMAIL_ACCOUNT, PASS)
except imaplib.IMAP4.error:
    logger.error("Failed to login")
    sys.exit(1)

# Selecting mailbox
returnval, data = Mailbox.select(MAILBOX)
if returnval != 'OK':
    logger.error("Could not open mailbox '{0}' with returnval: '{1}'".format(MAILBOX, returnval))

# Searching whether messages in mailbox
returnval, data = Mailbox.search(None, "ALL")
if returnval != 'OK':
    logger.error("No messages in mailbox")
    sys.exit(1)

# Processing mails in mailbox
for num in data[0].split():
    returnval, mail = Mailbox.fetch(num, '(RFC822)')
    if returnval != 'OK':
        logger.error("Could not get message {0}".format(num))
        sys.exit(1)
        
    do_something_with(mail)

Mailbox.close()
Mailbox.logout()
