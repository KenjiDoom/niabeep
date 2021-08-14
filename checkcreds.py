import smtplib, ssl
import os 
import getpass
import json
import base64 # maybe? 

# self note: First part of the program idea/concept 
def checkcreds():
    if os.path.exists('creds.json'): # self-note: Write if creds are valid 
        print('Testing credentials ')
        with open('creds.json') as data:
            data = json.load(data)
            gmail_server = smtplib.SMTP('smtp.gmail.com:587')
            gmail_server.starttls()
            try:
                gmail_server.login(data['email'], data['password'])
                resp = True
                print("Password Correct")
                gmail_server.quit()
                sending()
            except:
                resp = False
                gmail_server.quit()
                print("Incorrect Password")
                return resp
    
    else: # self-note: Check servers for validation 
        email = input("Email: ")
        password = getpass.getpass(prompt='Password: ', stream=None)
        gmail_server = smtplib.SMTP('smtp.gmail.com:587')
        gmail_server.starttls()
        try:
            gmail_server.login(email, password)
            resp = True
            print('Password Correct')
            creds = {
                    "email": "{}".format(email),
                    "password": "{}".format(password),
                    }
            json_object = json.dumps(creds, indent = 4)

            with open("creds.json", "w") as output:
                output.write(json_object)
                output.close()
        except:
            resp = False
            print('Incorrect Password')

        gmail_server.quit()
        return resp



def sending():
    with open('creds.json') as data:
        data = json.load(data)
        recv = input("To: ")
        subject = input("Subject: ")
        message = input("Message: ")
        text = """\
        {}

        """.format(subject) + message
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(data['email'], data['password'])
            server.sendmail(data['email'], recv, text)
            print('Sent')
        


checkcreds()
