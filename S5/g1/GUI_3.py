import tkinter as tk

root = tk.Tk()
lbl_counter = tk.Label(root, text=0)

counter = 0
def btn_callback():
    global counter
    counter += 1
    lbl_counter.config(text=str(counter))

btn_click_me = tk.Button(root, text='click me', command=btn_callback)

lbl_counter.pack()
btn_click_me.pack()
root.mainloop()