import tkinter as tk

# I have no idea as to what is going on

class app1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        #self.frame.pack(anchor='center')
        self.master.title('Authentication')

        self.frame1 = tk.Frame(self.master, width=250, height=250, relief='raise', bd=8)
        self.frame1.place(relx=0.5, rely=0.4, anchor='center')

        # Email Entry
        self.email = tk.Entry(self.frame1, text='Email ', bd=2, width=20, relief="solid")
        self.email.place(relx=0.5, rely=0.40, anchor="center")

        # Password Entry
        self.password = tk.Entry(self.frame1, text='Email', bd=2, width=20)
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
