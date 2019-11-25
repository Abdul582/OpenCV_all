import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2), np.uint8)
dialation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

title = ['image','Mask', 'dialation', 'erosion', 'opening', 'closing']
image = [img, mask, dialation, erosion, opening, closing]

for i in range(6):
    plt.subplot(3, 3, i+1), plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()