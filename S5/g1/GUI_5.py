import tkinter as tk

root = tk.Tk()
root.title('Frame')
frame = tk.Frame(root, width=400, height=300)
btn_test = tk.Button(frame, text='click me')

def motion_action(action):
    print(action.x, action.y)

frame.bind('<Motion>', motion_action)
btn_test.place(x=200, y=150)
frame.pack()
root.mainloop()