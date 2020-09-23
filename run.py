#! /usr/bin/env python3
__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/24/2020"

import read
import emails

def send_emails(name, message, mail_server):
    mail_server.send_message(message)
    print("Email Sent to {} : successfull".format(name))

if __name__ == '__main__':
    data = read.Data("email_list.csv")
    body = read.getBody("email_body.txt")
    sender = input("Please Enter Sender's Gmail: ")
    subject = input("Please Enter Subject Line: ")
    attatchment = input("Name.ext of attachement\n(leave blank for no attachment): ")
    mail_server = emails.authenticate(sender)
    for person in data:
        if attatchment.strip() == "":
            message = emails.generate_error_report(sender, person["email"], subject, body)
        else:
            message = emails.generate(sender, person["email"], subject, body, attatchment)
        send_emails(str(person["name"]), message, mail_server)
    #Log Out
    mail_server.quit()
    print("All mails sent successfully")
