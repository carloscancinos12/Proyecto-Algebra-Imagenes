from cProfile import label
from tabnanny import check
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import tkinter

root = Tk()
root.title("Imagenes Algebra")
root.geometry("300x520")
xbot = 20

archivo = '1.jpg'
imgIn = imageio.imread(archivo)
recorte = imgIn[110:440, 215:525]

#Funciones básicas para acciones del proyecto
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

def rotarGradosAH(Matriz, grados):
    if (grados == 90):
        rotada = rotarAH(Matriz)
        return rotada
    elif (grados == 180):
        rotada = rotarT(Matriz)
        return rotada 
    elif (grados == 270):
        rotada = rotarH(Matriz)
        return rotada
    elif (grados > 270):
        Matriz = rotarH(Matriz)
        grados = grados - 270
    elif (grados > 180):
        Matriz = rotarT(Matriz)
        grados = grados - 180
    elif (grados > 90):
        Matriz = rotarAH(Matriz)
        grados = grados - 90
    if (grados > 45):
        angulo = (90 - grados) * (np.pi / 180)
        Matriz = rotarAH(Matriz)
    else:
        angulo = grados * (np.pi / 180)
    f, c, p = Matriz.shape
    rotada = np.zeros((int(f + c*np.tan( angulo)), int(c + f*np.tan(angulo)), p), int)
    for capa in range(0,p):
        for fila in range(0,f):
            for columna in range(0,c):
                if (grados <= 45):
                    nuevaFila = int(fila + (c-columna)*np.tan(angulo))
                    nuevaColumna = int(columna + fila*np.tan(angulo))
                else:
                    nuevaFila = int(fila + columna*np.tan(angulo))
                    nuevaColumna = int(columna + (f - fila)*np.tan(angulo))
                rotada[nuevaFila, nuevaColumna, capa] = Matriz[fila, columna, capa]
    return rotada

def rotarGradosH(Matriz, grados):

    if (grados == 90):
        rotada = rotarH(Matriz)
        return rotada
    elif (grados == 180):
        rotada = rotarT(Matriz)
        return rotada
    elif (grados == 270):
        rotada = rotarAH(Matriz)
        return rotada
    elif (grados > 270):
        Matriz = rotarAH(Matriz)
        grados = grados - 270
    elif (grados > 180):
        Matriz = rotarT(Matriz)
        grados = grados - 180
    elif (grados > 90):
        Matriz = rotarH(Matriz)
        grados = grados - 90
    if (grados > 45):
        angulo = (90 - grados) * (np.pi / 180)
        Matriz = rotarH(Matriz)
    else:
        angulo = grados * (np.pi / 180)
    f, c, p = Matriz.shape
    rotada = np.zeros((int(f + c*np.tan( angulo)), int(c + f*np.tan(angulo)), p), int)
    for capa in range(0,p):
        for fila in range(0,f):
            for columna in range(0,c):
                if (grados <= 45):
                    nuevaFila = int(fila + columna*np.tan(angulo))
                    nuevaColumna = int(columna + (f - fila)*np.tan(angulo))
                else:
                    nuevaFila = int(fila + (c-columna)*np.tan(angulo))
                    nuevaColumna = int(columna + fila*np.tan(angulo))
                rotada[nuevaFila, nuevaColumna, capa] = Matriz[fila, columna, capa]
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

def RGB(Matriz1, R, G, B):
    aumentada = Matriz1.copy()
    fa ,ca ,pa = aumentada.shape
    print(pa)
    for i in range (fa):
        for j in range (ca):
            for k in range (pa):
                if(R == False and k == 0):
                    aumentada[i,j,k] = 0
                if(G == False and k == 1):
                    aumentada[i,j,k] = 0
                if(B == False and k == 2):
                    aumentada[i,j,k] = 0        
    return aumentada

def RGB_rec(Matriz1, R, G, B, x, y):
    aumentada = Matriz1.copy()
    fa ,ca ,pa = aumentada.shape
    print(pa)
    for i in range (int(x), int(x+100)):
        for j in range (int(y), int(y+100)):
            for k in range (pa):
                if(R == False and k == 0):
                    aumentada[i,j,k] = 0
                if(G == False and k == 1):
                    aumentada[i,j,k] = 0
                if(B == False and k == 2):
                    aumentada[i,j,k] = 0        
    return aumentada

#Entrys para el programa
Aument=StringVar()
Aument_entry = tkinter.Entry(root,textvariable=Aument)
Aument_entry.config(width=10)
Aument_entry.place(x=xbot+200,y=180)

Dismn=StringVar()
Dismn_entry = tkinter.Entry(root,textvariable=Dismn)
Dismn_entry.config(width=10)
Dismn_entry.place(x=xbot+200,y=230)

Posx=StringVar()
Posx_entry = tkinter.Entry(root,textvariable=Posx)
Posx_entry.config(width=10)
Posx_entry.place(x=xbot+200,y=270)

Posy=StringVar()
Posy_entry = tkinter.Entry(root,textvariable=Posy)
Posy_entry.config(width=10)
Posy_entry.place(x=xbot+200,y=295)

RotAnt=StringVar()
GradAH_entry = tkinter.Entry(root,textvariable=RotAnt)
GradAH_entry.config(width=10)
GradAH_entry.place(x=xbot+200,y=80)

RotHor=StringVar()
GradH_entry = tkinter.Entry(root,textvariable=RotHor)
GradH_entry.config(width=10)
GradH_entry.place(x=xbot+200,y=130)

PosxRGB=StringVar()
PosxRGB_entry = tkinter.Entry(root,textvariable=PosxRGB)
PosxRGB_entry.config(width=10)
PosxRGB_entry.place(x=xbot+200,y=450)

PosyRGB=StringVar()
PosyRGB_entry = tkinter.Entry(root,textvariable=PosyRGB)
PosyRGB_entry.config(width=10)
PosyRGB_entry.place(x=xbot+200,y=475)

#Labels
label1 = tkinter.Label(root, text="x veces")
label1.place(x=xbot+155, y=180)

label2 = tkinter.Label(root, text="x veces")
label2.place(x=xbot+155, y=230)

label3 = tkinter.Label(root, text="x")
label3.place(x=xbot+170, y=270)

label4 = tkinter.Label(root, text="y")
label4.place(x=xbot+170, y=295)

label5 = tkinter.Label(root, text="grados")
label5.place(x=xbot+155, y=80)

label6 = tkinter.Label(root, text="grados")
label6.place(x=xbot+155, y=130)

label3 = tkinter.Label(root, text="x")
label3.place(x=xbot+170, y=450)

label4 = tkinter.Label(root, text="y")
label4.place(x=xbot+170, y=475)

#Checkbox
boolR=BooleanVar()
CheckboxR=tkinter.Checkbutton(root,text="R",variable=boolR)
CheckboxR.place(x=xbot,y=420)

boolG=tkinter.BooleanVar()
CheckboxG=tkinter.Checkbutton(root,text="G",variable=boolG)
CheckboxG.place(x=xbot+50,y=420)

boolB=tkinter.BooleanVar()
CheckboxB=tkinter.Checkbutton(root,text="B",variable=boolB)
CheckboxB.place(x=xbot+100,y=420)

#Comandos para los botones
def ComandoAnHorario():
    plt.figure(figsize=(4,4))
    plt.imshow(rotarGradosAH(imgIn,int(GradAH_entry.get())))
    plt.show()

def ComandoHorario():
    plt.figure(figsize=(4,4))
    plt.imshow(rotarGradosH(imgIn,int(GradH_entry.get())))
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
    
def ComandoRGB():
    plt.figure(figsize=(4,4))
    plt.imshow(RGB(imgIn,boolR.get(),boolG.get(),boolB.get()))
    plt.show()
    
def ComandoRGB_Recor():
    plt.figure(figsize=(4,4))
    plt.imshow(RGB_rec(imgIn,boolR.get(),boolG.get(),boolB.get(), int(PosxRGB_entry.get()), int(PosyRGB_entry.get())))
    plt.show()
    
#Botones pantalla principal
boton1 = Button(root, text="Rotar Antihorario", width=20, height=2, command=ComandoAnHorario)
boton1.pack()
boton1.place(x=xbot,y=70)

boton2 = Button(root, text="Rotar Horario", width=20, height=2, command=ComandoHorario)
boton2.pack()
boton2.place(x=xbot,y=120)

boton3 = Button(root, text="Disminuir tamaño", width=20, height=2, command=ComandoReducir)
boton3.pack()
boton3.place(x=xbot,y=220)

boton4 = Button(root, text="Aumentar tamaño", width=20, height=2, command=ComandoAumentar)
boton4.pack()
boton4.place(x=xbot,y=170)

boton5 = Button(root, text="Original",width=20, height=2, command=ComandoOrig)
boton5.pack()
boton5.place(x=xbot,y=20)

boton6 = Button(root, text="desplazar", width=20, height=2, command=ComandoPosicion)
boton6.pack()
boton6.place(x=xbot,y=270)

boton7 = Button(root, text="sobreponer", width=20, height=2, command=ComandoTransponer)
boton7.pack()
boton7.place(x=xbot,y=320)

boton8 = Button(root, text="RGB", width=20, height=2, command=ComandoRGB)
boton8.pack()
boton8.place(x=xbot,y=370)

boton9 = Button(root, text="RGB recortado", width=20, height=2, command=ComandoRGB_Recor)
boton9.pack()
boton9.place(x=xbot,y=450)

root,mainloop()