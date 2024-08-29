import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from colorthief import *
import os

root=Tk()
root.title("Color Dectector")
root.geometry("800x600")
root.configure(bg="#1e201e")
root.resizable(False,False)


def showImage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",
                                                        filetype=(('PNG file','*.png'),
                                                                  ('JPG file','*.jpg'),
                                                                  ('ALL file','*.*')))
    

    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lb1.configure(image=img,width=310,height=270)
    lb1.image=img


def findColor():
    ct =  ColorThief(filename)
    palattte = ct.get_palette(color_count=11)

    rgb1 = palattte[0]
    rgb2 = palattte[1]
    rgb3 = palattte[2]
    rgb4 = palattte[3]
    rgb5 = palattte[4]
    rgb6 = palattte[5]
    rgb7 = palattte[6]
    rgb8 = palattte[7]
    rgb9 = palattte[8]
    rgb10 = palattte[9]

    color1 = f'#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}'
    color2 = f'#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}'
    color3 = f'#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}'
    color4 = f'#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}'
    color5 = f'#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}'
    color6 = f'#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}'
    color7 = f'#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}'
    color8 = f'#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}'
    color9 = f'#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}'
    color10 = f'#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}'

    colors1.itemconfig(id1,fill=color1)
    colors1.itemconfig(id2,fill=color2)
    colors1.itemconfig(id3,fill=color3)
    colors1.itemconfig(id4,fill=color4)
    colors1.itemconfig(id5,fill=color5)

    colors2.itemconfig(id6,fill=color6)
    colors2.itemconfig(id7,fill=color7)
    colors2.itemconfig(id8,fill=color8)
    colors2.itemconfig(id9,fill=color9)
    colors2.itemconfig(id10,fill=color10)

    hex1.config(text=color1)
    hex2.config(text=color2)
    hex3.config(text=color3)
    hex4.config(text=color4)
    hex5.config(text=color5)
    hex6.config(text=color6)
    hex7.config(text=color7)
    hex8.config(text=color8)
    hex9.config(text=color9)
    hex10.config(text=color10)


# icon
image_icon=PhotoImage(file="res\\icon.png")
root.iconphoto(False,image_icon)

Label(root,width=120,height=10,bg="#ecdfcc").pack()


# Frame
frame=Frame(root,width=700,height=500,bg="#3c3d37").place(x=50,y=50)


# Logo
logo=PhotoImage(file="res\\logo.png")
Label(frame,image=logo,bg="#3c3d37").place(x=150,y=50)

Label(frame,text="Color Detector",font="arial 40 bold",bg="#3c3d37",fg="white").place(x=250,y=60)

#colors1
colors1=Canvas(frame,bg="#d6deef",width=150,height=256,bd=0)
colors1.place(x=55,y=200)

id1 = colors1.create_rectangle((10,10,50,50),fill="#b8255f")
id2 = colors1.create_rectangle((10,50,50,100),fill="#db4035")
id3 = colors1.create_rectangle((10,100,50,150),fill="#ff9933")
id4 = colors1.create_rectangle((10,150,50,200),fill="#fad000")
id5 = colors1.create_rectangle((10,200,50,250),fill="#afb83b")

hex1 = Label(colors1,text="#b8255f",fg="#000",font="arial 12 bold",bg="#d6deef")
hex1.place(x=60,y=15)
hex2 = Label(colors1,text="#db4035",fg="#000",font="arial 12 bold",bg="#d6deef")
hex2.place(x=60,y=65)
hex3 = Label(colors1,text="#ff9933",fg="#000",font="arial 12 bold",bg="#d6deef")
hex3.place(x=60,y=115)
hex4 = Label(colors1,text="#fad000",fg="#000",font="arial 12 bold",bg="#d6deef")
hex4.place(x=60,y=165)
hex5 = Label(colors1,text="#afb83b",fg="#000",font="arial 12 bold",bg="#d6deef")
hex5.place(x=60,y=205)

# colors2
colors2=Canvas(frame,bg="#d6deef",width=150,height=256,bd=0)
colors2.place(x=210,y=200)

id6 = colors2.create_rectangle((10,10,50,50),fill="#7ecc45")
id7 = colors2.create_rectangle((10,50,50,100),fill="#299438")
id8 = colors2.create_rectangle((10,100,50,150),fill="#6accbc")
id9 = colors2.create_rectangle((10,150,50,200),fill="#158fad")
id10 = colors2.create_rectangle((10,200,50,250),fill="#14aa57")

hex6 = Label(colors2,text="#7ecc45",fg="#000",font="arial 12 bold",bg="#d6deef")
hex6.place(x=60,y=15)
hex7 = Label(colors2,text="#299438",fg="#000",font="arial 12 bold",bg="#d6deef")
hex7.place(x=60,y=65)
hex8 = Label(colors2,text="#6accbc",fg="#000",font="arial 12 bold",bg="#d6deef")
hex8.place(x=60,y=115)
hex9 = Label(colors2,text="#158fad",fg="#000",font="arial 12 bold",bg="#d6deef")
hex9.place(x=60,y=165)
hex10 = Label(colors2,text="#14aa57",fg="#000",font="arial 12 bold",bg="#d6deef")
hex10.place(x=60,y=205)


# select image
selectimage=Frame(frame,width=340,height=350,bg="#d6deef")
selectimage.place(x=370,y=150)

f = Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lb1=Label(f,bg="black")
lb1.place(x=0,y=0)

Button(selectimage,text="SELECT IMAGE",width=12,height=1,font="arial 14 bold",command=showImage).place(x=10,y=300)
Button(selectimage,text="FIND COLOR",width=12,height=1,font="arial 14 bold",command=findColor).place(x=176,y=300)

root.mainloop()