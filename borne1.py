#!//usr/bin/python3
# -*- coding: utf8 -*-

from tkinter import *
from PIL import *
import glob,sys,os

def reboot(event):
    os.system("reboot")

def close(event):
    os.system("shutdown -h now")

def start(event):
    os.system("scratch2")



fenetre =Tk()
fenetre.title('Technologie Collège')
fenetre.geometry('600x480')

label1=Label(fenetre,text='Borne ARCADE du collège')
label1.pack()

label2=Label(fenetre,text='Bienvenue dans le monde du RETROGAMING !')
label2.pack()

canvas = Canvas(fenetre,width=300,height=200)
canvas.pack()


my_image=PhotoImage(file='/home/pi/arcade/logo.png')
canvas.create_image(50,50, anchor=NW, image=my_image)


fenetre.bind('<r>',reboot)
fenetre.bind('<s>',start)
fenetre.bind('<e>',close)


label3=Label(fenetre, text='S-->Pour lancer Scratch2')
label3.pack()

label4=Label(fenetre, text='R-->Pour redémarrer la borne arcade')
label4.pack()

label5=Label(fenetre, text='E-->Pour éteindre')
label5.pack()

canvas2 = Canvas(fenetre,width=100,height=50)
canvas2.pack()
my_image2=PhotoImage(file='/home/pi/arcade/droitsCC.png')
canvas2.create_image(10,10, anchor=NW, image=my_image2)

label6=Label(fenetre, text='version 1.1')
label6.pack()

fenetre.mainloop()
