'''
This script is designed for administrative use to register a new user into the system's database.
After successful registration, an email is dispatched to the newly registered user.
The email contains a unique key that the user will use for Multi-Factor Authentication (MFA) registration.
The email is sent using port 465, which is designated for SMTPS (Simple Mail Transfer Protocol Secure).
SMTPS uses implicit TLS (Transport Layer Security), ensuring that the connection is encrypted from the outset.

'''

import smtplib
import os
import ssl
import datetime


# libraries to add attachement
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#database connection
import database

# function generating unique random key
import unique

yourkey=unique.generate_password()

db_path="path to database" # !! UPDATE to the path of database !! 


# password is stored in os environment
email_password=os.environ.get('environment variable') # !! UPDATE to the environment variable !!

db_entry=database.create_connection(db_path)

cursor = db_entry.cursor()

# admin register new user
email_to=input("Enter email address: ")
name=input ("Enter Name: ")
current_time=datetime.datetime.now()

#create connection to database
cursor.execute("INSERT INTO clients (email,username,date) VALUES(?,?,?)",(email_to, name,current_time))
db_entry.commit()
         

#create email
em = MIMEMultipart()
em['From']= 'youremail@mail.com' # !! UPDATE to your email address !!
em['To'] = email_to
em['Subject']='Introduction from FANG'

body=(f"""
     Hi {name}

     Should you choose to accept please register following the steps below:

     Step 1:
     Enter username specified in contract

     Step 2:
     Enter unique key (this code will self destruct in 24 hours):

        {yourkey}

    Step 3:
    Register for MFA 

    Step 4:
    Create your own unique password.

    from the .................

     """)

em.attach(MIMEText(body,'plain'))

#create a self signed SSL certificate for local(host) application.
context=ssl.create_default_context()

# initiating connection
with smtplib.SMTP_SSL('smtp.mail.com',465,context=context) as smtp: # !! UPDATE to your email smtp !!
    smtp.login('youremail@mail.com',email_password) # !! UPDATE to your email address !!
    smtp.sendmail('youremail@mail.com',email_to,em.as_string()) # !! UPDATE to your email address !!

#console log
print('email sent')


