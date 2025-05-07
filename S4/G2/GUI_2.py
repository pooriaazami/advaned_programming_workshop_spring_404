import tkinter as tk

root = tk.Tk()
root.title('Second App')

btn_click_me = tk.Button(text='click me')

btn_click_me.grid(columnspan=2, rowspan=2)

root.mainloop()
