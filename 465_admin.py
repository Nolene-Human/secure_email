
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


cursor.execute("INSERT INTO clients (email,username,date) VALUES(?,?,?)",(email_to, name,current_time))
db_entry.commit()
         
#create connection to database


#create email
em = MIMEMultipart()
em['From']= 'onlyforshowhack@gmail.com'
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


    "What's Done Is Done When We Say It's Done"

    from the FAMILY AREA NETWORK GANG

     """)

em.attach(MIMEText(body,'plain'))

#create a self signed SSL certificate for local(host) application.
context=ssl.create_default_context()

# initiating connection
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login('onlyforshowhack@gmail.com',email_password)
    smtp.sendmail('onlyforshowhack@gmail.com',email_to,em.as_string())

#console log
print('email sent')


#used in attachements
#from email.mime.application import MIMEApplication
#from email import encoders

# ---------------------------------------------------------------------- #

# IF I WANT TO ATTACH QR CODE

# ---------------------------------------------------------------------- #

# import pyotp #python OTP library
# import qrcode


# #generate user unique key that gets saved against their account when user register
# def key():
#     key=pyotp.random_base32()
#     return key

# #calls the key of the user (from database) and generates a QR code for the user to scan
# def generate_qr(key):
    
#     uri=pyotp.totp.TOTP(key).provisioning_uri(name="FANG",issuer_name="FANG App")
#     qr=qrcode.make(uri)#.save("QR.jpeg")
#     #print("QR.png",width=150)    
#     return qr

# def attach_file_to_email(email_message, filename):
#     # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
#     with open(filename, "rb") as f:
#         file_attachment = MIMEApplication(f.read())
#     # Add header/name to the attachments    
#     file_attachment.add_header(
#         "Content-Disposition",
#         f"attachment; filename= {filename}",
#     )
#     # Attach the file to the message
#     email_message.attach(file_attachment)


# key=key()

# content=f"""
# <!DOCTYPE html>
# <html>  
#     <body>
#         Hi {name}        
#         <h2 style="color:rgb(167, 22, 102)">Welcome to FANG</h2>

#         Here is your onetime passcode:



#     </body>
# </html>
# """
# body=MIMEText(content,'txt')
# em.attach(body)

# qr=generate_qr(key)#'QR.png'

# with open(qr, 'r') as q:
#     attachment=MIMEApplication(q.read())#, Name=basename(qr)
#     #attachment['Content-Disposition']='attachment;q="{}"'.format(basename(q))


# attach_file_to_email(em, 'QR.png')

