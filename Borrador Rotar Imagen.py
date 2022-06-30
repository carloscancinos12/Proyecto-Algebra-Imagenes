from tkinter import Button
import numpy as np
import imageio.v2 as imageio
from matplotlib import pyplot as plt
from matplotlib.widgets import Button

archivo = 'C:/Users/carlo/OneDrive/Escritorio/noaa.jpg'
imgIn = imageio.imread(archivo)
#plt.figure(figsize=(4,4))
#plt.imshow(imgIn)
#plt.show()

recorte = imgIn[110:440, 215:525]
plt.figure(figsize=(4,4))
plt.imshow(recorte)
plt.show()

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

def rotarGrados(Matriz, grados):

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

plt.figure(figsize=(4,4))
plt.imshow(rotarAH(recorte))
plt.show()

plt.figure(figsize=(4,4))
plt.imshow(rotarH(recorte))
plt.show()

plt.figure(figsize=(4,4))
plt.imshow(rotarT(recorte))
plt.show()

plt.figure(figsize=(4,4))
plt.imshow(aumentarDimensiones(recorte,5))
plt.show()

plt.figure(figsize=(4,4))
plt.imshow(disminuirDimensiones(recorte,2))
plt.show()

plt.figure(figsize=(4,4))
plt.imshow(rotarGrados(recorte,89))
plt.show()



