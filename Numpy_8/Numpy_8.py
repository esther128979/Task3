import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("Numpy_8\PIC.jpg")



print(img.shape)

red   = img[:, :, 0]
green = img[:, :, 1]
blue  = img[:, :, 2]


r_hist, _ = np.histogram(red, bins=256, range=(0, 256))
g_hist, _ = np.histogram(green, bins=256, range=(0, 256))
b_hist, _ = np.histogram(blue, bins=256, range=(0, 256))


plt.figure(figsize=(10,4))

plt.plot(r_hist, color='red')
plt.plot(g_hist, color='green')
plt.plot(b_hist, color='blue')

plt.title("RGB Histogram")
plt.xlabel("Color value (0-255)")
plt.ylabel("Pixel count")
plt.show()
