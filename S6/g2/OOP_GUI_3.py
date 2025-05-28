import tkinter as tk
from tkinter import ttk

    
class FirstFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

class SecondFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

class MainPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

        self.container = tk.Frame(self, width=400, height=300)

        self.f1 = FirstFrame(self.container)
        self.f2 = SecondFrame(self.container)

    def test(self):
        self.f1.tkiarse()

