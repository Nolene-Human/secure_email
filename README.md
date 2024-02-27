# Secure Email Application

This is a Python-based application designed to send secure emails. It uses Google's SMTP server and generates either a unique random key or One-Time-Passcode (OTP) QR Code for each email.

SMTP, or Simple Mail Transfer Protocol, is the standard protocol for email transmission on the internet. It uses different ports to send mail, mainly port 465 and port 587.

Port 465: This port is used for SMTPS, which stands for SMTP over SSL (Secure Sockets Layer). SSL is a cryptographic protocol that provides security for communications over networks. When you send an email using SMTP over SSL, your connection is encrypted and secure, which means that the email content is protected from being read by other users on the internet.

Port 587: This port is used for MSA (Mail Submission Agent). It was introduced to be used for email submission, specifically for clients to send email messages to a mail server. Port 587 also supports STARTTLS, a protocol command that allows an in-use connection to be upgraded to an encrypted (TLS or SSL) connection instead of using a separate port for secure communication.

In summary, both ports are used for secure email transmission, but port 465 uses implicit SSL/TLS, while port 587 uses explicit SSL/TLS (STARTTLS).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- A Google account

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository
2. Install the required Python packages using pip:

# Send Secure Email

3. Set up your Google account for SMTP access.
    Resources:
    https://www.youtube.com/watch?v=1YXVdyVuFGA

## Running the tests

You will need to update 465_admin.py, 587_admin.py and reply.py wiht your gmail account and key for the files to run.
You will need to personalise your OTP.py file name to your application name.

run python reply.py


## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Google SMTP Server](https://www.google.com/) - Used to send emails

## Authors

* **Nolene Human** - [Nolene-Human](https://github.com/Nolene-Human)


## Acknowledgments

* Hat tip to anyone whose code was used
* Sombex @sombex

