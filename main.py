from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

final = np.asarray(Image.open("ayanimage.jpg")).copy()

imgplot = plt.imshow(original)


for row in range(len(final)):
    final[row] = final[row][::-1]


imgplot = plt.imshow(final)
plt.show()