import tkinter as tk

# I have no idea as to what is going on

class app1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title('Authentication')

        self.frame1 = tk.Frame(self.master, width=250, height=270, relief='raise', bd=8)
        self.frame1.pack(anchor='center')

        self.display_email = tk.Label(self.frame, text='Email ', width=8).pack()
        self.email = tk.Entry(self.frame, text='email', bd=2, width=15).pack()
        #self.email.bind(0, "Password: ")

        self.btn1 = tk.Button(self.frame, text = 'Login', bg='#32B448', fg='white', width = 10, command = self.login).pack(side='left')
        self.btn2 = tk.Button(self.frame, text='Quit', width=10, command = self.close_window).pack(side='right')
        #self.email = tk.Entry(self.frame, width=20, text='Email: ', bg='#32B448').pack()
        #self.email.pack(side='bottom')

        #self.frame = tk.Frame(self.master, width=250, height=270, relief='raise', bd=8)
        self.frame.pack()


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
