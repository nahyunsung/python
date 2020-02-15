import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

#이미지 출력 함수
def disp_ing(path):
    #경로 Path의 이미지 불러오기
    newImage = PIL.Image.open(path)

    #불러온  이미지를 레이블에 출력하기
    imageData = PIL.ImageTk.PhotoImage(newImage)
    lbl_ing.configure(image=imageData)
    lbl_ing.image = imageData

#파일 오픈 함수 선언
def open_File():
    fpath = fd.askopenfilename()

    if fpath:
        #print(fpath)
        #lbl_ing.configure(text=fpath)
        disp_ing(fpath)


#윈도우 창 생성
root = tk.Tk()
root.geometry("400x350")

#버튼과 레이블 생성
btn = tk.Button(text="파일 열기", command = open_File)
lbl_ing = tk.Label()

#컨트롤(버튼, 레이블) 화면에 배치
btn.pack()
lbl_ing.pack()

#화면 유지
tk.mainloop()
