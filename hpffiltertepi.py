import cv2
import numpy as np
from matplotlib import pyplot as plt
#import library numpy dan cv2/opencv
#Matplotlib hadir dengan fungsi merencanakan histogram: matplotlib.pyplot.hist (). Ini langsung menemukan histogram dan plot itu. Anda tidak perlu menggunakan fungsi calcHist () atau np.histogram () untuk menemukan histogram.

# loading image
#img = cv2.imread('photo.jpg')
img = cv2.imread('photo.jpg',)

# converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)
#menginisialisai gambar & merubahnya menjadi efek kabur Gaussian(efek gaussian untuk menghilangkan noise)

# convolute with proper kernels
laplacian = cv2.Laplacian(img, cv2.CV_64F) #efek laplacian, cv2.CV_64F untuk meminta ukuran gambar tujuan.  
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) #sobelx menginisialisasi gambar menjadi efek sobel x-dir
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) #sobely menginisialisasi menjadi efek sobel y-dir terhadap axes Y

#untuk menampilkan hasil gambar kedalam satu figure
plt.subplot(2,2,1), plt.imshow(img,cmap = 'gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show() 