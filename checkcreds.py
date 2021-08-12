import smtplib, ssl
import os 
import getpass
import json
import base64


# self note: First part of the program idea/concept 
def checkcreds():
    if os.path.exists('creds.json'): # self-note: Write if creds are valid 
        print('NOW OPEN THE FILE AND TEST THE PASSWORD') 
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
            print('Password Wrong Try Again..')

        gmail_server.quit()
        return resp





checkcreds()
