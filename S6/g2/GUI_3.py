import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

def command():
    print(value.get())

value = tk.IntVar(value=4)
rd_btn_1 = ttk.Radiobutton(frame, value=1, 
                           text='Option 1', 
                           variable=value)

rd_btn_2 = ttk.Radiobutton(frame, value=2, 
                           text='Option 2', 
                           variable=value)

rd_btn_3 = ttk.Radiobutton(frame, value=3, 
                           text='Option 3', 
                           variable=value)

btn = ttk.Button(frame, text='Read Data', command=command)

rd_btn_1.place(x=50, y=50)
rd_btn_2.place(x=50, y=80)
rd_btn_3.place(x=50, y=110)
btn.place(x=50, y=140)

frame.pack()
root.mainloop()