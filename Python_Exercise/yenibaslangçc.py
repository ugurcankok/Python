import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\Casper\\Desktop\\indir.jpg', cv2.IMREAD_COLOR )
img1=cv2.imread('C:\\Users\\Casper\\Desktop\\indir.jpg',0)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = - 1
ret,thresh1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
mask = np.zeros(img1.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img1,img1,mask = mask)
# Histogramı maskeli ve maskesiz olarak hesapladık
# Maske için üçüncü argümanı kontrol ettik
hist_full = cv2.calcHist([img1],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img1],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img1, )
#plt.subplot(222), plt.imshow(mask,'gray')
#plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(222), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()

cv2.imshow('image',img)
cv2.imshow('image1',img1)
cv2.imshow('image2',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
