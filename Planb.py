from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import tkinter

root = Tk()
root.title("Imagenes Algebra")
root.geometry("400x200")

archivo = '1.jpg'
imgIn = imageio.imread(archivo)
recorte = imgIn[110:440, 215:525]

Aument=StringVar()
Aument_entry = tkinter.Entry(root,textvariable=Aument)
Aument_entry.config(width=10)
Aument_entry.place(x=220,y=80)

Dismn=StringVar()
Dismn_entry = tkinter.Entry(root,textvariable=Dismn)
Dismn_entry.config(width=10)
Dismn_entry.place(x=30,y=80)

Posx=StringVar()
Posx_entry = tkinter.Entry(root,textvariable=Posx)
Posx_entry.config(width=10)
Posx_entry.place(x=150,y=130)
Posy=StringVar()
Posy_entry = tkinter.Entry(root,textvariable=Posy)
Posy_entry.config(width=10)
Posy_entry.place(x=150,y=150)

def reflejarY(Matriz):
    f, c, p = Matriz.shape
    reflejada = np.zeros((f, c, p), int)
    for capa in range(0,p):
        for fila in range(0,f):
            reflejada[fila,:,capa] = Matriz[fila,::-1,capa]
    return reflejada

def rotarAH(Matriz):
    f, c, p = Matriz.shape
    rotada = np.zeros((c, f, p), int)
    reflejada = reflejarY(Matriz)
    for capa in range(0, p):
        rotada[:,:,capa] = reflejada[:,:,capa].T
    return rotada

def reflejarX(Matriz):
    f, c, p = Matriz.shape
    reflejada = np.zeros((f, c, p), int)
    for capa in range(0,p):
        for columna in range(0,c):
            reflejada[:,columna,capa] = Matriz[::-1,columna,capa]
    return reflejada

def rotarH(Matriz):
    f, c, p = Matriz.shape
    rotada = np.zeros((c, f, p), int)
    reflejada = reflejarX(Matriz)
    for capa in range(0, p):
        rotada[:,:,capa] = reflejada[:,:,capa].T
    return rotada

def rotarT(Matriz):
    f, c, p = Matriz.shape
    rotada = np.zeros((f, c, p), int)
    rotada = reflejarX(Matriz)
    rotada = reflejarY(rotada)
    return rotada

def aumentarFilas(Matriz, aumentoD):
    f, c, p = Matriz.shape
    duplicada = np.zeros(((aumentoD * f), c, p), int)
    for capa in range(0,p):
        for fila in range(0,f):
            for aum in range(0,aumentoD):
                duplicada[((fila*aumentoD) + aum),:,capa] = Matriz[fila,:,capa]
    return duplicada

def aumentarColumnas(Matriz, aumentoD):
    f, c, p = Matriz.shape
    duplicada = np.zeros((f, (c * aumentoD), p), int)
    for capa in range(0,p):
        for columna in range(0,c):
            for aum in range(0,aumentoD):
                duplicada[:,((columna*aumentoD) + aum),capa] = Matriz[:,columna,capa]
    return duplicada

def aumentarDimensiones(Matriz, aumentoD):
    f, c, p = Matriz.shape
    aumentada = np.zeros(((f + (f//aumentoD)), (c + (c//aumentoD)), p), int)
    aumentada = aumentarFilas(Matriz, aumentoD)
    aumentada = aumentarColumnas(aumentada, aumentoD)
    return aumentada

def disminuirFilas(Matriz, disminucionD):
    f, c, p = Matriz.shape
    duplicada = np.zeros((int(f / disminucionD), c, p), int)
    for capa in range(0,p):
        for fila in range(0,f):
            if (fila%disminucionD) == 0:
                duplicada[int(fila / disminucionD),:,capa] = Matriz[fila,:,capa]
    return duplicada

def disminuirColumnas(Matriz, disminucionD):
    f, c, p = Matriz.shape
    duplicada = np.zeros((f, int(c / disminucionD), p), int)
    for capa in range(0,p):
        for columna in range(0,c):
            if (columna%disminucionD) == 0:
                duplicada[:,int(columna / disminucionD),capa] = Matriz[:,columna,capa]
    return duplicada

def disminuirDimensiones(Matriz, aumentoD):
    f, c, p = Matriz.shape
    aumentada = np.zeros(((f + (f//aumentoD)), (c + (c//aumentoD)), p), int)
    aumentada = disminuirFilas(Matriz, aumentoD)
    aumentada = disminuirColumnas(aumentada, aumentoD)
    return aumentada
def cambiarpos(Matriz, posx,posy):
    f, c, p = Matriz.shape
    aumentada = np.zeros((f+posy, c+posx, p), int)
    for fila in range(0,f):
        for columna in range(0,c):
            aumentada[fila+posy,columna+posx,:]=Matriz[fila,columna,:]
    return aumentada
def ComandoHorario():
    plt.figure(figsize=(4,4))
    plt.imshow(rotarH(imgIn))
    plt.show()
    
def ComandoAnHorario():
    plt.figure(figsize=(4,4))
    plt.imshow(rotarAH(imgIn))
    plt.show()
    
def ComandoAumentar():
    plt.figure(figsize=(4,4))
    plt.imshow(aumentarDimensiones(imgIn,int(Aument_entry.get())))
    plt.show()
    
def ComandoReducir():
    plt.figure(figsize=(4,4))
    plt.imshow(disminuirDimensiones(imgIn,int(Dismn_entry.get())))
    plt.show()
    
def ComandoOrig():
    plt.figure(figsize=(4,4))
    plt.imshow(imgIn)
    plt.show()
def ComandoPosicion():
    plt.figure(figsize=(4,4))
    plt.imshow(cambiarpos(imgIn,int(Posx_entry.get()),int(Posy_entry.get())))
    plt.show()

boton1 = Button(root, text="Rotar Antihorario", command=ComandoAnHorario)
boton1.pack()
boton1.place(x=30,y=20)

boton2 = Button(root, text="Rotar Horario", command=ComandoHorario)
boton2.pack()
boton2.place(x=220,y=20)

boton3 = Button(root, text="Disminuir tamaño", command=ComandoReducir)
boton3.pack()
boton3.place(x=30,y=100)

boton4 = Button(root, text="Aumentar tamaño", command=ComandoAumentar)
boton4.pack()
boton4.place(x=220,y=100)

boton5 = Button(root, text="Original", command=ComandoOrig)
boton5.pack()
boton5.place(x=130,y=60)
boton6 = Button(root, text="desplazar", command=ComandoPosicion)
boton6.pack()
boton6.place(x=150,y=100)
root,mainloop()