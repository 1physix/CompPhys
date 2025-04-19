#IMPORTS
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

fig, ax = plt.subplots()


#Defining the axes boundaries for the image
ax.set_xlim(-8.0, 8.0)
ax.set_ylim(-4.0, 4.0)
plt.figure(figsize=(10,10))


#Adding grid lines and spacing them
ax.grid(True)
ax.set_xticks(np.arange(-8.0, 8.1, 1.0))
ax.set_yticks(np.arange(-4.0, 4.1, 0.5))


#Adding x-axis vertical line for mirror
ax.axvline(0, color = "red", linestyle = "dashed", linewidth = "2")
ax.text(-0.75, 4.1, 'mirror', color='red')

#Name x and y axes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.tick_params(left=False, bottom=False)




final = np.asarray(Image.open("ayanimage.jpg")).copy()




plt.show()