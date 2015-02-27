#!/usr/bin/python

import datetime
import os, sys
import sendEmail

########## VARS ##############
path = "/home/ftp/lfbcdi/"
machines = ['machineCDI', 'machineBCD', 'machineMarmoteca']
subjectEmail = "Respaldo de BCDI"
##############################

mylist = []
today = datetime.date.today()
mylist.append(today)

textEmail = ""
textEmail += "Fecha : " + str(mylist[0]) + "\n\n"


# if its a working day (Monday to Friday) we expect to receive a bak file
if today.weekday()<5: 
  
  # date of today under the format yyyymmdd
  dateOfToday = ''.join(str(mylist[0]).split('-'))

  # list of files at $path
  files = os.listdir( path )

  for m in machines:
    machine = m + "-backupBCDI-" + dateOfToday 
    textEmail += "Maquina : " + m + "\n"
    textEmail += "Se subio un respaldo : " + str(any(machine in s for s in files)) + "\n\n"

  sendEmail.sendEmail(subjectEmail, textEmail, toEmail)
