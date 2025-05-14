import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

def check_command():
    print(var.get())

var = tk.BooleanVar()
check_box = ttk.Checkbutton(frame,
                            text='Option 1', 
                            variable=var, 
                            command=check_command)

check_box.place(x=50, y=50)

frame.pack()
root.mainloop()