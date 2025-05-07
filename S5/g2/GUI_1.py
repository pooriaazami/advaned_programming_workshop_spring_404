import tkinter as tk

root = tk.Tk()

turn = True
def toggle():
    global turn
    if turn:
        btn_test.config(text='X')
    else:
        btn_test.config(text='O')

    turn = not turn

btn_test = tk.Button(root, text='X', command=toggle)

btn_test.pack()
root.mainloop()