import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

menu = tk.Menu(frame)
file_menu = tk.Menu(menu)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Exit')
file_menu.add_separator()
file_menu.add_command(label='Info')
menu.add_cascade(label='file', menu=file_menu)

edit_menu = tk.Menu(menu)
edit_menu.add_command(label='Chnage font')
edit_menu.add_command(label='Save database')
menu.add_cascade(label='edit', menu=edit_menu)

frame.pack()
root.config(menu=menu)
root.mainloop()