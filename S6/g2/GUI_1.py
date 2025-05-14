import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

def btn_command():
    print(entry.get())
    var.set('')

var = tk.StringVar()
entry = ttk.Entry(frame, textvariable=var) # show='*'
btn = ttk.Button(frame, text='Read Data', command=btn_command)

entry.place(x=50, y=50)
btn.place(x=50, y=80)

frame.pack()
root.mainloop()