import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, width=400, height=300)
btn_click_me = tk.Button(frame, text='click me!')

def motion(event):
    print(event.x, event.y)

frame.bind('<Motion>', motion)
btn_click_me.place(x=200, y=150)
frame.pack()
root.mainloop()
