import tkinter as tk

# I have no idea as to what is going on

class app1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('Authentication')

        # The big white frame
        self.frame1 = tk.Frame(self.master, width=250, height=270, relief='raise', bd=8)
        self.frame1.place(relx=0.5, rely=0.4, anchor='center')

        # Login Message Text
        self.login_message = tk.Label(self.frame1, width=20, text='Login into your account', relief='raise', font=("Times", 14))
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
        self.password = tk.Entry(self.frame1, text='Password', bd=1, width=25)
        self.password.place(relx=0.5, rely=0.60, anchor="center")

        # Login Button
        self.btn1 = tk.Button(self.frame1, text = 'Login', bg='#32B448', fg='white', width = 10, command = self.login)
        self.btn1.place(relx=0.5, rely=0.80, anchor="center")

        # Quit button
        #self.btn2 = tk.Button(self.frame1, text='Cancel', width=4, command = self.close_window)
        #self.btn2.pack(anchor="center")

        self.frame.pack(anchor='center')


    def close_window(self):
        self.master.destroy()

    def login(self):
        pass


def main():
    root = tk.Tk()
    root.geometry("400x400")
    root['background']='#1091E4'
    root.resizable(False, False)
    app = app1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
