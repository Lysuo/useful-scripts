#! /usr/bin/python

import datetime
import os

mylist = []
today = datetime.date.today()
mylist.append(today)
dateOfToday = ''.join(str(mylist[0]).split('-'))

# bak of svl-server sqlite db
nameBak = 'db.sqlite3.svl-' + dateOfToday
os.system("cp /webapps/svl-server-py/svl_server_py/db.sqlite3 /home/backups/"+nameBak)

# bak of django-portfolio sqlite db
nameBak = 'db.sqlite3.django-portfolio-' + dateOfToday
os.system("cp /webapps/django-portfolio/django_portfolio_blog/db.sqlite3 /home/backups/"+nameBak)

# delete backups older than 7 days
os.system("find /home/backups/db.sqlite3.* -mtime +7 -exec rm {} \;")
