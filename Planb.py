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

def rotarGrados(Matriz, grados):

    if (grados == 90):
        rotada = rotarAH(Matriz)
        return rotada

    elif (grados == 180):
        rotada = rotarH(Matriz)
        return rotada
    
    elif (grados == 270):
        rotada = rotarT(Matriz)
        return rotada

    elif (grados > 270):
        Matriz = rotarT(Matriz)
        grados = grados - 270

    elif (grados > 180):
        Matriz = rotarH(Matriz)
        grados = grados - 180

    elif (grados > 90):
        Matriz = rotarAH(Matriz)
        grados = grados - 90

    f, c, p = Matriz.shape
    angulo = grados * (np.pi / 180)
    rotada = np.zeros((int(f + c*np.tan(angulo)), int(c + f*np.tan(angulo)), p), int)
    for capa in range(0,p):
        for fila in range(0,f):
            for columna in range(0,c):
                nuevaFila = fila + (c-columna)*np.tan(angulo) - 7
                nuevaColumna = columna + fila*np.tan(angulo) - 7
                nuevaFila = int(nuevaFila)
                nuevaColumna = int(nuevaColumna)
                rotada[nuevaFila, nuevaColumna, capa] = Matriz[fila, columna, capa]
                for x in range(0,int(grados/15)):
                    for y in range(0,int(grados/15)):
                        rotada[(nuevaFila+x), nuevaColumna, capa] = Matriz[fila, columna, capa]
                        rotada[nuevaFila, (nuevaColumna+y), capa] = Matriz[fila, columna, capa]
                        rotada[(nuevaFila+x), (nuevaColumna+y), capa] = Matriz[fila, columna, capa]
    return rotada
def Transponer(Matriz1, Matriz2,posx,posy):
    f1, c1, p1 = Matriz1.shape
    f2, c2, p2 = Matriz2.shape 
    aumentada = np.zeros((f1+f2, c1+c2, p1), int)
    fa ,ca ,pa = aumentada.shape

    for fila in range(0,f1):
        for columna in range(0,c1):
            aumentada[fila,columna,:]=Matriz1[fila,columna,:]
    for fila in range(0,f2):
        for columna in range(0,c2):
            aumentada[fila+posx,columna+posy,:]=Matriz2[fila,columna,:]    
    return aumentada
Aument=StringVar()
Aument_entry = tkinter.Entry(root,textvariable=Aument)
Aument_entry.config(width=10)
Aument_entry.place(x=140,y=80)

Dismn=StringVar()
Dismn_entry = tkinter.Entry(root,textvariable=Dismn)
Dismn_entry.config(width=10)
Dismn_entry.place(x=140,y=50)

Posx=StringVar()
Posx_entry = tkinter.Entry(root,textvariable=Posx)
Posx_entry.config(width=10)
Posx_entry.place(x=150,y=130)

Posy=StringVar()
Posy_entry = tkinter.Entry(root,textvariable=Posy)
Posy_entry.config(width=10)
Posy_entry.place(x=150,y=150)
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
def ComandoTransponer():
    plt.figure(figsize=(4,4))
    plt.imshow(Transponer(imgIn,imgIn,50,50))
    plt.show()
boton1 = Button(root, text="Rotar Antihorario", command=ComandoAnHorario)
boton1.pack()
boton1.place(x=30,y=20)

boton2 = Button(root, text="Rotar Horario", command=ComandoHorario)
boton2.pack()
boton2.place(x=220,y=20)

boton3 = Button(root, text="Disminuir tamaño", command=ComandoReducir)
boton3.pack()
boton3.place(x=30,y=50)

boton4 = Button(root, text="Aumentar tamaño", command=ComandoAumentar)
boton4.pack()
boton4.place(x=30,y=80)

boton5 = Button(root, text="Original", command=ComandoOrig)
boton5.pack()
boton5.place(x=135,y=20)
boton6 = Button(root, text="desplazar", command=ComandoPosicion)
boton6.pack()
boton6.place(x=150,y=100)

boton7 = Button(root, text="sobreponer", command=ComandoTransponer)
boton7.pack()
boton7.place(x=30,y=110)
root,mainloop()