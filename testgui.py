import cv2
from tkinter import *
from PIL import Image,ImageTk

camera=cv2.VideoCapture(0)

master=Tk()
master.title('computer vision')
master.maxsize(width=640,height=480)
master.minsize(width=640,height=480)

tk_frame=Frame(master,width=640,height=480)
tk_frame.grid(row=0,column=0)


lb=Label(tk_frame)
lb.grid(row=0,column=0)


def video_frame():
    ret1, frame=camera.read()
    frame=cv2.resize(frame,(640,480))
    conversion=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    process_img=Image.fromarray(conversion)
    imgtk=ImageTk.PhotoImage(image=process_img)
    lb.imgtk=imgtk
    lb.configure(image=imgtk)
    lb.after(1,video_frame)


video_frame()
master.mainloop()
