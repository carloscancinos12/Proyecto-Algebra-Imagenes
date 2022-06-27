from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

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




def ComandoHorario():
    plt.figure(figsize=(4,4))
    plt.imshow(rotarH(recorte))
    plt.show()
    
def ComandoAnHorario():
    plt.figure(figsize=(4,4))
    plt.imshow(rotarAH(recorte))
    plt.show()
    
def ComandoAumentar():
    None
    
def ComandoReducir():
    None


boton1 = Button(root, text="Rotar Antihorario", command=ComandoAnHorario)
boton1.pack()
boton1.place(x=30,y=20)

boton2 = Button(root, text="Rotar Horario", command=ComandoHorario)
boton2.pack()
boton2.place(x=220,y=20)

boton3 = Button(root, text="Disminuir tamaño", command=ComandoAumentar)
boton3.pack()
boton3.place(x=30,y=100)

boton4 = Button(root, text="Aumentar tamaño", command=ComandoReducir)
boton4.pack()
boton4.place(x=220,y=100)

root,mainloop()