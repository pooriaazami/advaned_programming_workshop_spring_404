import tkinter as tk

root = tk.Tk()
flag = [True for _ in range(2)]

turn = True
def click(btn):
    global turn
    if btn == 1 and flag[btn-1]:
        if turn:
            btn_1.config(text='X')
        else:
            btn_1.config(text='O')
    elif btn == 2 and flag[btn-1]:
        if turn:
            btn_2.config(text='X')
        else:
            btn_2.config(text='O')

    turn = not turn
    flag[btn-1] = False

btn_1 = tk.Button(root, text='1', command=lambda: click(1))
btn_2 = tk.Button(root, text='2', command=lambda: click(2))

btn_1.pack()
btn_2.pack()

root.mainloop()