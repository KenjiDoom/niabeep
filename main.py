import smtplib, getpass
import ssl
port = 465

print("Using Gmail Service...")

email = input("Email: ")

password = getpass.getpass(prompt='Password: ', stream=None)

recv = input("Receiver: ")

subject= input("Subject: ")

#message = input("Message: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)
    server.sendmail(email, recv, subject) 
    print('Sent.') 
