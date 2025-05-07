import tkinter as tk

root = tk.Tk()

first_lbl = tk.Label(root, text='1'*10)
second_lbl = tk.Label(root, text='2'*10)

first_lbl.grid(row=0, column=0)
second_lbl.grid(row=0, column=1)

root.mainloop()