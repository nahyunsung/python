import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

#이미지 출력 함수
def dispPhoto(path):
    # 경로 path의 이미지 불러오기
    newImage = PIL.Image.open(path).resize( (300, 300) )

    # 불러온 이미지를 레이블에 출력하기
    imageData =  PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

    lbl.configure(text = "파일 주소 : %s" %(path))

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")
lbl = tk.Label(text = "")


btn = tk.Button(text = "파일열기", command=openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
lbl.pack()

tk.mainloop()
