import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5), np.float)/25
dest = cv2.filter2D(img, -1, kernal)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bileteralfilter = cv2.bilateralFilter(img, 9, 75,75)

title = ['image', '2D convolution', 'blur', 'GaussianBlur', 'median', 'bileteralfilter']
image = [img, dest, blur, gblur, median, bileteralfilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()