import tkinter as tk

# I have no idea as to what is going on

class app1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master['background']='#1091E4'
        self.master.title('Authentication')
        self.master.geometry('400x400') # self-note: This should not be here
        self.master.resizable(False, False) # self-note: This too prolly
        self.btn1 = tk.Button(self.frame, text = 'Login', bg='#32B448', fg='white', width = 20, command = self.login).pack(side='bottom')
        self.btn2 = tk.Button(self.frame, text='Quit', width=20, command = self.close_window).pack()
        self.frame.pack()


    def close_window(self):
        pass

    def login(self):
        pass



def main():
    root = tk.Tk()
    app = app1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
