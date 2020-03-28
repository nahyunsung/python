import random as r
import tkinter as tk

def num():
    global q_num
    as_num = int(a_num.get())
    if as_num == q_num:
        lbl.configure(text = "정답 !!")
        txtnum.configure(state = 'readonly')
    elif as_num > q_num:
        lbl.configure(text = "더작은 수자를 넣어봐!!")
    else:
        lbl.configure(text= "더큰 숫자를 넣어봐!!" )

root = tk.Tk()
root.geometry("300x300")

q_num = r.randint(1,100)
a_num = tk.StringVar()

print(q_num)

lbl = tk.Label(text = "정답은 ???")
txtnum = tk.Entry(textvariable = a_num)
btn = tk.Button(text="정답", command = num)

lbl.pack()
txtnum.pack()
btn.pack()

tk.mainloop()