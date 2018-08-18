from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master


root = Tk()
app = Window(root)
root.mainloop()