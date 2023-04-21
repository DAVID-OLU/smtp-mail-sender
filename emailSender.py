# For the program to work, you need to : 
# go over to your gmail account and setup 2 factor authentication.
# generate app password. Then after that, store that generated password in an environment variable in your 
# control panel, and then use the variable here in your program code.


from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'ogunsinqatar@gmail.com'
email_password = input("")

email_receiver = input("Enter Receiver Email: ")

subject = input("Enter your Subject here: ")
body = input("Enter your Message here: ")


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

