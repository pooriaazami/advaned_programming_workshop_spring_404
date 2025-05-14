import tkinter as tk
from tkinter import ttk

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.container = tk.Frame(self, width=400, height=300)

        self.frame_1 = tk.Frame(self.container, width=100, height=100, background='red')
        self.frame_2 = tk.Frame(self.container, width=100, height=100, background='blue')
        self.btn = ttk.Button(self.container, text='Swap', command=self.btn_command)

        self.flag = True

        self.frame_2.place(x=50, y=50)
        self.frame_1.place(x=50, y=50)
        self.btn.place(x=250, y=250)
        self.container.pack()

    def btn_command(self):
        if self.flag:
            self.frame_1.tkraise()
        else:
            self.frame_2.tkraise()

        self.flag = not self.flag

main_page = MainPage()
main_page.mainloop()