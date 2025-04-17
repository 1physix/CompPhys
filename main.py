from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open("ayanimage.jpg"))


imgplot = plt.imshow(img)
plt.show()