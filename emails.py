#!/usr/bin/env python3
__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/23/2020"

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message

def generate_error_report(sender, recipient, subject, body):
  """Creates an email without an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  return message

def authenticate(sender):
    #Login into Email Server and send Email from it
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_pass = input("Enter password for {} to send email...".format(sender))
    code = mail_server.login(sender, mail_pass)
    print(code)
    return  mail_server

