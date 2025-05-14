import tkinter as tk
from tkinter import ttk

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.container = tk.Frame(self, width=400, height=300)
        self.change_btn = ttk.Button(self.container, text='switch', command=self.btn_command)
        self.frame_1 = tk.Frame(self.container, width=200, height=200, background='red')
        self.frame_2 = tk.Frame(self.container, width=200, height=200, background='blue')

        self.active_frame = True

        self.frame_1.place(x=20, y=20)
        self.frame_2.place(x=20, y=20)
        self.change_btn.place(x=300, y=250)
        self.container.pack() 
        
    def btn_command(self):
        if self.active_frame:
            self.frame_2.tkraise()
        else:
            self.frame_1.tkraise()

        self.active_frame = not self.active_frame

main = MainPage()
main.mainloop()
    