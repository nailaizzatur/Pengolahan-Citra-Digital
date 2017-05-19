import cv2
import numpy as np
from matplotlib import pyplot as plt
#import library numpy dan cv2/opencv
#Matplotlib hadir dengan fungsi merencanakan histogram: matplotlib.pyplot.hist (). Ini langsung menemukan histogram dan plot itu. Anda tidak perlu menggunakan fungsi calcHist () atau np.histogram () untuk menemukan histogram.

# loading image
#img = cv2.imread('photo.jpg')
img = cv2.imread('photo.jpg')
# converting to gray scale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#rumus equalization
equ = cv2.equalizeHist(gray_img)

cv2.imshow('Gambar Asli',gray_img)
cv2.imshow('Histogram Equalization', equ)

#menampilkan gambar Histogram Equalization
plt.figure('Histogram Awal')   
plt.hist(gray_img.ravel(),300,[0,256]),plt.title('Histogram awal')  
plt.figure('Histogram Equalization')  
plt.hist(equ.ravel(),256,[0,256]),plt.title('Histogram hasil equalization')
plt.show()

while True:
     k = cv2.waitKey(0) & 0xFF
     if k == 27 : break           # ESC key to exit
cv2.destroyAllWindows()