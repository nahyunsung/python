import tkinter as tk
import random

def dis_label():
    a = list(range(1,46))
    random.shuffle(a)
    lbl.configure(text=a[:6])

#200 x 100 픽셀 창 만들기
root = tk.Tk()
root.geometry("200x100")

#레이블과 버튼
lbl = tk.Label(text = "")
btn = tk.Button(text="로또", command=dis_label)

lbl.pack()
btn.pack()
tk.mainloop()