#!/usr/bin/env python

######### /!\ #############
#
# you will need the sendEmail.py file to get this working as it is
# in addition get the myIp.py file or set up an empty myIp.py file with just 
# myIp = ''
# into it, put the file in the same dir
#
###########################

import os
import myIp
import sendEmail as se

ip  = os.popen('wget -qO- http://ipecho.net/plain').readlines()

if ip[0] != myIp.myIp:
  se.sendEmail('subject : ip changed', 'The new ip is ' + ip[0] + '.', 'whotomailitto@mail.com') 

  output = open("myIp.py", "w")
  output.write("myIp = ")
  output.write("'"+ip[0]+"'")
  output.close()
