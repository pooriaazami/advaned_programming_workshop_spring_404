import tkinter as tk

root = tk.Tk()
root.title('First GUI App')

lbl_name = tk.Label(root, text='Hello, World!!')

lbl_name.pack()
root.mainloop()