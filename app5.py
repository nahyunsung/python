#이름과 나이 테스트 상자 만들기
#app5

import tkinter as tk

def dispLabl():
    cal_old = int(txt_old.get())
    lbl.configure(text = "%s님, 내년에 %d살 입니다."% (txt_name.get(),cal_old + 1))
#윈도우 생성

root = tk.Tk()
root.geometry("200x100")

#텍스트 상자 값 저장 변수 선언
name = tk.StringVar()
old = tk.StringVar()

#윈도우 컨트롤 생성
lbl = tk.Label(text="")
txt_name = tk.Entry(textvariable=name)
txt_old = tk.Entry(textvariable=old)
btn = tk.Button(text="PUSH", command=dispLabl)

#윈도우 컨트롤 배치
lbl.pack()
txt_name.pack()
txt_old.pack()
btn.pack()

tk.mainloop()