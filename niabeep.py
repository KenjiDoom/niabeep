from tkinter import messagebox
import tkinter as tk
import smtplib, ssl
import os
import json


class app2: # Sending Emails
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('Gmail Email Sender')
        # Who the message is being sent too
        self.to = tk.Entry(self.master, width=30, text='To', relief='raise')
        self.to.place(relx=0.5, rely=0.1, anchor='s')

        # Subject of the message
        self.subject = tk.Entry(self.master, width=30, text='Subject: ', relief='raise')
        self.subject.place(relx=0.5, rely=0.3, anchor='s')

        self.frame.pack(anchor='center')

#-------------------------------------------------#
class app(): # Self-Note: Fix Error Box Not closing correctly
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('Authentication')

        # The big white frame
        self.frame1 = tk.Frame(self.master, width=250, height=270, relief='raise', bd=8)
        self.frame1.place(relx=0.5, rely=0.4, anchor='center')

        # Login Message Text
        self.login_message = tk.Label(self.frame1, width=20, text='Login into your account', relief='flat', font=("Times", 14))
        self.login_message.place(relx=0.5, rely=0.10, anchor="center")

        self.email_message = tk.Label(self.frame1, width=10, text='Email: ', relief='flat', font=("Times", 11))
        self.email_message.place(relx=0.15, rely=0.28, anchor="center")

        # Email Entry
        self.email = tk.Entry(self.frame1, text='Email', bd=1, width=25)
        self.email.place(relx=0.5, rely=0.35, anchor="center")

        # Password Message Text
        self.password_message = tk.Label(self.frame1, width=10, text='Password: ', relief='flat', font=("Times", 11))
        self.password_message.place(relx=0.20, rely=0.52, anchor="center")

        # Password Entry
        self.password = tk.Entry(self.frame1, show='*', bd=1, width=25)
        self.password.place(relx=0.5, rely=0.60, anchor="center")

        # Login Button
        self.btn1 = tk.Button(self.frame1, text = 'Login', bg='#32B448', fg='white', width = 8, command = self.login)
        self.btn1.place(relx=0.3, rely=0.80, anchor="center")

        # Cancel button
        self.btn2 = tk.Button(self.frame1, text='Cancel', bg='#b41f24', fg='white', width=8, command = self.close_window)
        self.btn2.place(relx=0.7, rely=0.80, anchor="center")

        self.frame.pack(anchor='center')

    def close_window(self):
        self.master.destroy()

    def login(self):
        email = self.email.get()
        password = self.password.get()
        gmail_server = smtplib.SMTP('smtp.gmail.com:587')
        gmail_server.starttls()
        try:
            gmail_server.login(email, password)
            resp = True
            print('Password Correct') # START NEW CLASS WINDOW AND CLOSE OLD WINDOW
            #sender_gui()
            creds = {
                    "email": "{}".format(email),
                    "password": "{}".format(password),
            }
            json_object = json.dumps(creds, indent = 4)

            with open('creds.json', "w") as output:
                output.write(json_object)
                output.close()
                sender_gui()
        except: # add pop-up box message
            resp = False
            messagebox.showerror('oops',  'Incorrect email or password')
            self.password.delete(0, 'end')

        gmail_server.quit()
        return resp

#----------------------------------------------#

def login_gui(): # Self-Note: Login UI
    root = tk.Tk()
    root.geometry("400x400")
    root['background']='#1091E4'
    root.resizable(False, False)
    login_gui = app(root)
    root.mainloop()


def sender_gui(): # Self-Note: Email Sender UI
    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(False, False)
    sender_gui = app2(root)
    root.mainloop()

#-------------------------------------------------#
def auto():# Self-note: This is where the automation happens. The scanning for creds and checking if they exists or not
    if os.path.exists('creds.json'):
        print('Testing Creds...')
        with open('creds.json') as data:
            data = json.load(data)
            gmail_server = smtplib.SMTP('smtp.gmail.com:587')
            gmail_server.starttls()
            try:
                gmail_server.login(data['email'], data['password'])
                resp = True
                sender_gui()
            except:
                resp = False
                gmail_server.quit()
                return resp
                login_gui()
    else:
        login_gui()



if __name__ == '__main__':
    sender_gui()
