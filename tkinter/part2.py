from tkinter import *


class MyApp:

    def __init__(self, master):
        self.master = master
        self.master.title = "MyGUI"
        self.init()

    def init(self):
        btn1 = Button(self.master, text="button")
        btn2 = Button(self.master, text="button")
        btn3 = Button(self.master, text="button", command=self.command)

        btn1.grid(row=1, column=0, padx=1,pady=1)
        btn2.grid(row=1, column=1, padx=1,pady=1)
        btn3.grid(row=1, column=2, padx=1,pady=1)

    def command(self):
        self.lb = Label(self.master, text="Hello world")
        self.lb.grid(row=2, column=2)

master = Tk()
master.geometry("100x300")
myapp = MyApp(master)
master.mainloop()