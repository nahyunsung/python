import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disp_photo(path):
    #이미지 불러오기
    newImage = PIL.Image.open(path)

    # 이미지 크기 계산하기
    mywidth = 300
    sizefac = mywidth / newImage.size[0]
    myheight = int(newImage.size[1]*sizefac)
    print(newImage.size)
    print(mywidth, myheight)
    newImage = newImage.resize((mywidth, myheight))

    #이미지 라벨에 표시하기
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.imge = imageData

    imageData = PIL.ImageTk.PhotoImage(newImage.convert("L"))
    mimageLabel.configure(image=imageData)
    mimageLabel.imge = imageData

def open_file():
    fpath = fd.askopenfilename()

    if fpath:
        disp_photo(fpath)
root = tk.Tk()
root.geometry("400x900")

btn = tk.Button(text="open", command = open_file)
imageLabel = tk.Label()
mimageLabel = tk.Label()

btn.pack()
imageLabel.pack()
mimageLabel.pack()

tk.mainloop()