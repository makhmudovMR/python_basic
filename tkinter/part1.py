from tkinter import Tk, Label, Button

"""
Create a class which be our app
"""
class MyFirstGUI:
    def __init__(self, master):
        self.master = master # take the tk object which is an basic component in tk app
        master.title("A simple GUI") # init title for gui app

        self.label = Label(master, text="This is our first GUI!")
        self.label.place(x=0,y=0)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()