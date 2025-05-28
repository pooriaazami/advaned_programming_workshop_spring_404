import tkinter as tk
from tkinter import ttk

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.container = tk.Frame(self, width=400, height=300)

        self.f1 = tk.Frame(self.container, width=200, height=200, background='blue')
        self.f2 = tk.Frame(self.container, width=200, height=200, background='red')
        self.btn = ttk.Button(self.container, text='swap', command=self.swap_frames)
        
        self.flag = True

        self.btn.place(x=300, y=200)
        self.f1.place(x=10, y=10)
        self.f2.place(x=10, y=10)

        self.container.pack()

    def swap_frames(self):
        if self.flag:
            self.f1.tkraise()
        else:
            self.f2.tkraise()

        self.flag = not self.flag

if __name__ == '__main__':
    main = MainPage()
    main.mainloop()

        