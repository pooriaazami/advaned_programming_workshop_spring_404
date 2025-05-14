import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

def btn_command():
    print(entry.get())
    var.set('')

var = tk.StringVar(value='Default Value')
entry = ttk.Entry(frame, textvariable=var) # show='*'
btn = ttk.Button(frame, text='read data', command=btn_command)

entry.place(x=150, y=100)
btn.place(x=150, y=130)

frame.pack()
root.mainloop()