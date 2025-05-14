import tkinter as tk
from tkinter import ttk

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.btn = ttk.Button(self, text='Click me!', command=self.btn_command)
        self.btn.pack()

    def btn_command(self):
        print('Hello')

main_page = MainPage()
main_page.mainloop()