import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

def check_box_command():
    print(value.get())

value = tk.BooleanVar(value=True)
check_button = ttk.Checkbutton(frame, variable=value, text='Some option', command=check_box_command)

check_button.place(x=50, y=50)

frame.pack()
root.mainloop()