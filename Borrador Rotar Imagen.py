import numpy as np
import imageio.v2 as imageio
from matplotlib import pyplot as plt

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

def pruebaFilas(Matriz, aumentoD):
    f, c, p = Matriz.shape
    duplicada = np.zeros(((aumentoD * f), c, p), int)
    for capa in range(0,p):
        for fila in range(0,f):
            for aum in range(0,aumentoD):
                duplicada[((fila*aumentoD) + aum),:,capa] = Matriz[fila,:,capa]
    return duplicada

def pruebaColumnas(Matriz, aumentoD):
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
    aumentada = pruebaFilas(Matriz, aumentoD)
    aumentada = pruebaColumnas(aumentada, aumentoD)
    return aumentada

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



