#문제 풀기
#app6

import tkinter as tk
import random as r

def disp_Label():
    int_ans = int(txt_ans.get())
    if int_ans == a+s:
        lal.configure(text = "정답")
    else:
        lal.configure(text = "오답")

#윈도우 생성
root = tk.Tk()
root.geometry("200x100")

a = r.randrange(1, 100)
s = r.randrange(1, 100)

ans = tk.StringVar()

lbl = tk.Label(text = " %d+%d = " % (a,s))
lal = tk.Label(text = "")
txt_ans = tk.Entry(textvariable=ans)
btn = tk.Button(text="풀기", command = disp_Label)

lbl.pack()
txt_ans.pack()
btn.pack()
lal.pack()

tk.mainloop()