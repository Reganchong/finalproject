import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

#!/usr/bin/env python
# coding: utf-8

# In[7]:


import easyocr
import numpy as np
import cv2
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageDraw,ImageTk
import matplotlib.pyplot as plt




# In[2]:


reader = easyocr.Reader(['ja','en'],gpu=False,model_storage_directory='./model')


# In[3]:




test=['image/test0.jpg','image/test1.jpg','image/test2.jpg','image/test3.jpg','image/test4.jpg','image/test5.jpg','image/test6.jpg','image/test7.jpg','image/test8.jpg','image/test9.jpg','image/test10.jpg','image/test11.jpg','image/test12.jpg','image/test13.jpg','image/test14.jpg','image/test15.jpg']
test2=['./image/test0.jpg','./image/test1.jpg','./image/test2.jpg','./image/test3.jpg','./image/test4.jpg','./image/test5.jpg','./image/test6.jpg','./image/test7.jpg','./image/test8.jpg','./image/test9.jpg','./image/test10.jpg','./image/test11.jpg','./image/test12.jpg','./image/test13.jpg','./image/test14.jpg','./image/test15.jpg']
imgcrop=['crop/crop0.jpg','crop/crop1.jpg','crop/crop2.jpg','crop/crop3.jpg','crop/crop4.jpg','crop/crop5.jpg','crop/crop6.jpg','crop/crop7.jpg','crop/crop8.jpg','crop/crop9.jpg','crop/crop10.jpg','crop/crop11.jpg','crop/crop12.jpg','crop/crop13.jpg','crop/crop14.jpg','crop/crop15.jpg']
check=["bfimg/checked0.jpg","bfimg/checked1.jpg","bfimg/checked2.jpg","bfimg/checked3.jpg","bfimg/checked4.jpg","bfimg/checked5.jpg","bfimg/checked6.jpg","bfimg/checked7.jpg","bfimg/checked8.jpg","bfimg/checked9.jpg","bfimg/checked10.jpg","bfimg/checked11.jpg","bfimg/checked12.jpg","bfimg/checked13.jpg","bfimg/checked14.jpg","bfimg/checked15.jpg"]


# In[4]:


def select():
    global x
    x = int(x_entry.get())
    return 


def present(x):
    global img
    print('目標圖片')
    img = Image.open(test[x])
    plt.imshow(img)
    plt.show()
    
def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img

def oas():
    
    im = cv_imread(test[x])
    cv2image = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA)
    img1 = cv2.resize(cv2image, (260, 400))
    img = Image.fromarray(img1)
    imgtk = ImageTk.PhotoImage(image=img)
    video.imgtk = imgtk
    video.configure(image=imgtk)
    


def oas2():
    
    im = cv_imread(check[x])
    cv2image = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA)
    img1 = cv2.resize(cv2image, (260, 400))
    img = Image.fromarray(img1)
    imgtk = ImageTk.PhotoImage(image=img)
    video1.imgtk = imgtk
    video1.configure(image=imgtk)
    
def oas3():
    
    im = cv_imread(imgcrop[x])
    cv2image = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA)
    img1 = cv2.resize(cv2image, (260, 90))
    img = Image.fromarray(img1)
    imgtk = ImageTk.PhotoImage(image=img)
    video2.imgtk = imgtk
    video2.configure(image=imgtk)
    
def readandsquare():
    result = reader.readtext(test[x])
    img = Image.open(test[x])
    draw = ImageDraw.Draw(img)
    for i in result:
        draw.rectangle((tuple(i[0][0]),tuple(i[0][2])),fill=None,outline='red',width=2)
    img.save(check[x])
    oas2()
    word()
    
    
def word():
    global result
    result = reader.readtext(test[x],detail=0)
    label3['text'] = result
    

def croptittle():
    img = Image.open(test[x])
    width, height = img.size 
    # Setting the points for cropped image 
    left = width/20
    top = height / 30
    right = 19*width/20
    bottom = height / 8
    # Cropped image of above dimension 
    # (It will not change orginal image) 
    img1 = img.crop((left, top, right, bottom)) 
    img1.save(imgcrop[x])
    oas3()
    word2()

def word2():
    
    result2 = reader.readtext(imgcrop[x],detail=0)
    label5['text'] = result2


# In[6]:


# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('文字檢測（讀卡機）')

# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("1200x700+150+50")


label = tk.Label(window,                 # 文字標示所在視窗
                 text = "input you select from 1 to 15:")  # 顯示文字

# 以預設方式排版標示文字
label.grid(row=0,column=0)



# 建立按鈕



x_entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width = 20) # 輸入欄位的寬度
x_entry.grid(row=0,column=1)

button = tk.Button(window,          # 按鈕所在視窗
                   text = '確定',  # 顯示文字
                   command = select) # 按下按鈕所執行的函數

# 以預設方式排版按鈕
button.grid(row=0,column=2)


button = tk.Button(window,          # 按鈕所在視窗
                   text = '顯示圖片',  # 顯示文字
                   command = oas) # 按下按鈕所執行的函數

# 以預設方式排版按鈕
button.grid(row=1,column=0)

button2 = tk.Button(window,          # 按鈕所在視窗
                   text = '偵測文字',  # 顯示文字
                   command = readandsquare) # 按下按鈕所執行的函數

# 以預設方式排版按鈕
button2.grid(row=1,column=1)

videoFrame = tk.Frame(window).grid()
video = tk.Label(videoFrame)
video.grid(row=2,column=0)

videoFrame1 = tk.Frame(window).grid()
video1 = tk.Label(videoFrame1)
video1.grid(row=2,column=1)

label2 = tk.Label(window,                 # 文字標示所在視窗
                 text = "檢測到的文字：")  # 顯示文字

# 以預設方式排版標示文字
label2.grid(row=3,column=0)

label3 = tk.Label(window,                 # 文字標示所在視窗
                 text = "",
                 wraplength = 800,)  # 顯示文字

# 以預設方式排版標示文字
label3.grid(row=3,column=1)



button3 = tk.Button(window,          # 按鈕所在視窗
                   text = '剪切標題並偵測文字',  # 顯示文字
                   command = croptittle) # 按下按鈕所執行的函數

# 以預設方式排版按鈕
button3.grid(row=4,column=0)

label4 = tk.Label(window,                 # 文字標示所在視窗
                 text = "檢測到的標題：")  # 顯示文字

# 以預設方式排版標示文字
label4.grid(row=5,column=0)


label5 = tk.Label(window,                 # 文字標示所在視窗
                 text = "")  # 顯示文字

# 以預設方式排版標示文字
label5.grid(row=5,column=1)

videoFrame2 = tk.Frame(window).grid()
video2 = tk.Label(videoFrame2)
video2.grid(row=6,column=1)

# 執行主程式
window.mainloop()


# In[ ]:





# In[ ]:




