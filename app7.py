#app7
#비만도 측정

import tkinter as tk

#윈도우 만들기(200x100)
root = tk.Tk()
root.geometry("200x100")

#변수 선언(키, 몸무게, BMI)
height = tk.StringVar()
weight = tk.StringVar()

#BMI 결과 출력 함수(disp_Label)
def disp_Label():
    h = int(txt_height.get())
    w = int(txt_weight.get())
    bmi = w/ ((h/100)*(h/100))
    if bmi <= 18.5:
        msg = "저체중"
    elif bmi <= 23:
        msg = "정상"
    elif bmi <= 25:
        msg = "과체중"
    else:
        msg =  "비만"
    lbl.configure(text="BMI 지수: %.2f, 판정: %s" %(bmi, msg))


#컨트롤 생성
txt_height = tk.Entry(textvariable=height)
txt_weight = tk.Entry(textvariable=weight)
btn = tk.Button(text = "측정", command = disp_Label)
lbl = tk.Label(text="")


#윈도우 컨트롤 배치
txt_height.pack()
txt_weight.pack()
btn.pack()
lbl.pack()

tk.mainloop()