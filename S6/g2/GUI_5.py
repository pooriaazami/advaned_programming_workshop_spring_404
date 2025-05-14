import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

root_menu = tk.Menu(frame)

file_menu = tk.Menu(root_menu)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Close')
file_menu.add_separator()
file_menu.add_command(label='Info')
root_menu.add_cascade(label='file', menu=file_menu)

frame.pack()
root.config(menu=root_menu)
root.mainloop()