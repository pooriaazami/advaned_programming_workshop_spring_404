import tkinter as tk

root = tk.Tk()
root.title('This is my first GUI app')

# lbls = []
# for i in range(3):
#     for j in range(3):
#         idx = j + i * 3

#         lbl = tk.Label(text=str(idx)*10)
#         lbl.grid(row=i, column=j)

#         lbls.append(lbl)

# def action():
#     print('You clicked a button!')

# btn_first_button = tk.Button(root, text='click me!', command=action)

# btn_first_button.pack()

counter = 0
lbl_count = tk.Label(root, text='0')

def increase():
    global counter
    counter += 1
    lbl_count.config(text=str(counter))

btn_increase = tk.Button(root, text='click me!', command=increase)

lbl_count.grid(row=0, column=0)
btn_increase.grid(row=0, column=1)

root.mainloop()
