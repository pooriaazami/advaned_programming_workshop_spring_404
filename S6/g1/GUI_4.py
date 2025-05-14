import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

def command():
    print(cmb.get())


cmb = ttk.Combobox(frame, values=[f'Option {i}' for i in range(1, 11)])
btn = ttk.Button(frame, text='read data', command=command)

cmb.place(x=50, y=50)
btn.place(x=50, y=80)

frame.pack()
root.mainloop()