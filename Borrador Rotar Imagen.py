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

plt.figure(figsize=(4,4))
plt.imshow(rotarAH(recorte))
plt.show()

plt.figure(figsize=(4,4))
plt.imshow(rotarH(recorte))
plt.show()

plt.figure(figsize=(4,4))
plt.imshow(rotarT(recorte))
plt.show()



