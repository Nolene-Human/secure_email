import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import OTP

#key=OTP.key()
#OTP.generate_qr(key)

def send_email_with_qr():
    from_address = "onlyforshowhack@gmail.com"
    to_address = "nhuman101@gmail.com"
    subject = "QR Code"
    body = "Please find the attached QR code."

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach the QR code
    filename = "QR.png"
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    message.attach(part)

    # Connect to the server
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    # Login to the email server
    server.login(from_address, "your password") # !! UPDATE to your gmail app password!!

    # Send the email
    text = message.as_string()
    server.sendmail(from_address, to_address, text)

    # Logout and close the connection
    server.quit()

send_email_with_qr()