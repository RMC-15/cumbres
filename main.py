import tkinter as tk                # python 3
from tkinter import font as tkfont

import variables
from login import Login
from menu import Cumbres

variables.userp='RMC'
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.container = tk.Frame(master=self, width=300, height=130, bg='blue')
        self.container.grid(row=0, column=0)
        self.container.config(bg="lightblue")
        self.container.config(bd=3)
        self.iconbitmap('icono.ico')
        #container.config(relief="sunken")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Cumbres):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()