import tkinter as tk

root = tk.Tk()

btns = []
n = 10
for i in range(n):
    row = []
    for j in range(n):
        btn = tk.Button(root, text="*")
        btn.grid(row=i, column=j)
        row.append(btn)
    btns.append(row)

if btns[0][0].cget('text') == "*":
    print("Hey")

root.mainloop()