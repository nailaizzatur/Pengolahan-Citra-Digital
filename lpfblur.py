import cv2
import numpy as np
from matplotlib import pyplot as plt
#import library numpy dan cv2/opencv
#Matplotlib hadir dengan fungsi merencanakan histogram: matplotlib.pyplot.hist (). Ini langsung menemukan histogram dan plot itu. Anda tidak perlu menggunakan fungsi calcHist () atau np.histogram () untuk menemukan histogram.

# loading image
#img = cv2.imread('photo.jpg')
img = cv2.imread('photo.jpg')

blur = cv2.blur(img,(5,5))
blur2 = cv2.GaussianBlur(img,(5,5),0)

#untuk menampilkan hasil gambar kedalam satu figure
plt.subplot(2,2,1),plt.imshow(img),plt.title('Gambar Asli')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(blur),plt.title('Blured')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(blur2),plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([]))

plt.show()