
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('onlyforshowhack@gmail.com','zdoo wual qujw fvtv')

email=input("Enter email address: ")

name=input ("Enter Name: ")

send=input( "Send payment y/n: ")

server.sendmail('onlyforshowhack@gmail.com',email,'"Hi from Fang port 587')

print('mail sent')