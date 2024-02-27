'''
This script is a simpler script designed to send a simple email using port 587,  
If possible, the connection will auto-negotiate to encrypted TLS5. If this fails, the email sending process will fall back to plain text and send as normal. 
This is the preferred method as one port can handle both plaintext and TLS

NOTE: Update using 465_admin.py to make more secure
'''

import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('youremail@mail.com','password') # !! UPDATE to your email address and password!!

email=input("Enter email address: ")

name=input ("Enter Name: ")

send=input( "Send payment y/n: ")

server.sendmail('youremail@mail.com',email,'"Hi from .....') # !! UPDATE to your email address !!

print('mail sent')
