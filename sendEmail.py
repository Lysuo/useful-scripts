#! /usr/bin/python

import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(subjectMail, textMail, toEmail):
  
  # Addresses
  me = "sendingemail@mail.com"
  mypass = "mypasswordforthisaccount"
  mystmpserver = "smtpserverurl"
  you = toEmail 

  # Message
  msg = MIMEMultipart('alternative')
  msg['Subject'] = subjectMail 
  msg['From'] = me
  msg['To'] = you
  part1 = MIMEText(textMail, 'plain')
  msg.attach(part1)

  # Sending
  server = smtplib.SMTP(mystmpserver, 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(me, mypass)
  text = msg.as_string()
  server.sendmail(me, you, text)
  server.quit()
