from tkinter import messagebox
import tkinter as tk
import smtplib, ssl
import os
import json

class app2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('Gmail Email Sender')

        # Who the message is being sent too
        self.too = tk.Label(self.master, width=10, bd=1.5, text='To:', relief='flat', font=("Times"))
        self.too.place(relx=0.2, rely=0.1, anchor='e')

        self.to = tk.Entry(self.master, width=33, text='To', relief='flat', bd=1.5)
        self.to.place(relx=0.5, rely=0.1, anchor='center')

        # Subject of the message
        self.sub = tk.Label(self.master, width=10, text='Subject:', relief='flat', font=("Times"))
        self.sub.place(relx=0.2, rely=0.2, anchor='e')

        self.subject = tk.Entry(self.master, width=33, text='Subject: ', relief='flat')
        self.subject.place(relx=0.5, rely=0.2, anchor='center')

        # Message Frame
        self.frame1 = tk.Frame(self.master)
        self.frame1.place(relx=0.4, rely=0.62, anchor='center', width=380, height=350)

        # Text box
        self.message = tk.Text(self.frame1, bg='white', fg='black',)
        self.message.pack(fill='both', pady=5, padx=5, expand=True)

        # Send Button
        self.send = tk.Button(self.master, width=7, text='Send', relief='flat', fg='black', bg='#32B448', font=("Times"), command = self.sending)
        self.send.place(relx=0.9, rely=0.62, anchor='center')

        # Cancel button
        self.cancel = tk.Button(self.master, width=7, text='Cancel', relief='flat', fg='black', bg='#ff0000', font=("Times"), command = self.close_window)
        self.cancel.place(relx=0.9, rely=0.67, anchor='center')

        self.frame.pack(anchor='center')


    def sending(self):
        to = self.to.get()
        subject = self.subject.get()
        message = self.message.get("1.0",'end-1c')
        email_construction = 'Subject: {}\n\n{}'.format(subject, message)
        with open('creds.json') as data:
            data = json.load(data)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(data['email'], data['password'])
                server.sendmail(data['email'], to, email_construction)
                messagebox.showinfo('SENT',  'SENT')

    def close_window(self):
        self.master.destroy()

class app():
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
            creds = {
                    "email": "{}".format(email),
                    "password": "{}".format(password),
            }
            json_object = json.dumps(creds, indent = 4)

            with open('creds.json', "w") as output:
                output.write(json_object)
                output.close()
                self.master.destroy()
                sender_gui()
        except:
            resp = False
            messagebox.showerror('oops',  'Incorrect email or password')
            self.password.delete(0, 'end')

        gmail_server.quit()
        return resp


def login_gui():
    root = tk.Tk()
    root.geometry("400x400")
    root['background']='#1091E4'
    root.resizable(False, False)
    login_gui = app(root)
    root.mainloop()


def sender_gui():
    root = tk.Tk()
    root.geometry("500x500")
    root['background']='#1091E4'
    root.resizable(False, False)
    sender_gui = app2(root)
    root.mainloop()


def auto():
    if os.path.exists('creds.json'):
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
    auto()
