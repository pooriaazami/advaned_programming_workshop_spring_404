import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)

cmb = ttk.Combobox(frame, values=[f'Option {i}' for i in range(1, 11)])

cmb.place(x=50, y=50)

frame.pack()
root.mainloop()