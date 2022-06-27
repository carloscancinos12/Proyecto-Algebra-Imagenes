import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import NonUniformImage
from matplotlib import cm
import imageio.v2 as imageio
archivo = 'img/1.jpg'
imgIn = imageio.imread(archivo)
fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
ax = axs[0, 0]
ax.set_xlim(-64, 64)
ax.set_ylim(-4, 4)
plt.imshow(imgIn)
archivo = 'img/1.png'
imgIn = imageio.imread(archivo)
ax=axs[0,1]
plt.imshow(imgIn)
plt.show()