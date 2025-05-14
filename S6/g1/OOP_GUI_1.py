import tkinter as tk
from tkinter import ttk

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.container = tk.Frame(self, width=400, height=300)
        # self.lbl = ttk.Label(self.container, text='...')
        self.btn_click_me = ttk.Button(self.container, text='Click me', command=self.btn_command)

        self.container.pack()
        self.btn_click_me.place(x=50, y=50)

    def btn_command(self):
        print('Btn Clicked!')

if __name__ == '__main__':
    main_page = MainPage()
    main_page.mainloop()
