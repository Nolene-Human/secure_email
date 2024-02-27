'''
PTES Pre-engagement Interaction
Step 3: Email new customer OTP QR code. 
'''


import smtplib
import os
from os.path import basename
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import ssl
import html

import OTP

email=input("Enter email address: ")

name=input ("Enter Name: ")

send=input( "Send payment y/n: ")

if send=='y':
            
            FROM = 'youremail@gmail.com'  # UPDATE with your email 
            PASSWORD=os.environ.get('gmail') # UPDATE with your key
            TO = email
                
            subject=f"Welcome from FANG"
            content =f" Hi before you we begin you will need to register OTP" 
            em = MIMEMultipart()
            em['From']=FROM
            em['To']=TO
            em['Subject']=subject
            body=MIMEText(content,'plain')
            em.attach(body)

            context = ssl.create_default_context()
            
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                    smtp.login(FROM, PASSWORD)
                    smtp.sendmail(FROM,TO,em.as_string())
                
            except Exception as ex:
                print(ex) 
