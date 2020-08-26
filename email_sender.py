import smtplib
from email.message import EmailMessage

sender_name = input("What is your name? ")
recipient = input("What is the email for the recipient? ")
email_password = input("What is the password? ")
subject_line = input("What is the subject line? ")
email_content = input("What do you want to say? ")

email = EmailMessage()
email['from'] = sender_name
email['to'] = recipient
email['subject'] = subject_line

email.set_content(email_content)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    # connect securely
    smtp.starttls()
    smtp.login(recipient, email_password)
    smtp.send_message(email)
    print('All good!')