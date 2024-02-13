
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('youremail@mail.com','password') # !! UPDATE to your email address and password!!

email=input("Enter email address: ")

name=input ("Enter Name: ")

send=input( "Send payment y/n: ")

server.sendmail('youremail@mail.com',email,'"Hi from Fang port 587') # !! UPDATE to your email address !!

print('mail sent')
