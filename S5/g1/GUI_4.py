import tkinter as tk

root = tk.Tk()


lbl_text = tk.Label(root, text='')
text = ''
def btn_action(btn):
    global text

    text += btn
    lbl_text.config(text=text)
    
btn_1 = tk.Button(root, text=1, command=lambda : btn_action('1'))
btn_2 = tk.Button(root, text=2, command=lambda: btn_action('2'))

lbl_text.grid(row=0, column=0, columnspan=2)
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)

root.mainloop()