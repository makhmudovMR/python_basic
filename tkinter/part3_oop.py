import tkinter as tk


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)#?
        container.grid_rowconfigure(0, weight=1)#?
        container.grid_columnconfigure(0, weight=1)#?

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="start page")
        label.pack(pady=10, padx=10)

        # button = tk.Button(self, text="Hello world")
        # button.pack(side="left", padx=10, pady=10)

myapp = MyApp()
myapp.mainloop()
