import numpy as np
import cv2

img1 = cv2.imread('apple.jpg')
img2 = cv2.imread('orange.jpg')

print(img1.shape)
print(img1.shape)
app_orng = np.hstack((img1[:,:256], img2[:,256:]))

#generate gaussian pyramid

apple = img1.copy()
gp_apple = [apple]

for i in range(6):
    apple_layer = cv2.pyrDown(apple[i])
    gp_apple.append(apple_layer)

orange = img2.copy()
gp_orange = [orange]

for i in range(6):
    orange_layer = cv2.pyrDown(orange[i])
    gp_orange.append(orange_layer)

#generate lapacian pryamid

# apple = gp_apple[5]
# lp_apple = [apple]
#
# for i in range(5, 0, -1):
#     gp_extend = cv2.pyrUp(gp_apple[i])
#     laplacian = cv2.subtract(gp_apple[i-1], gp_extend)
#     lp_apple.append(laplacian)

# generate Laplacian Pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

# generate Laplacian Pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

# orange_cp = gp_orange[5]
# lp_orange = [orange_cp]
#
# for i in range(5, 0, -1):
#     gp_extend = cv2.pyrUp(gp_orange[i])
#     laplacian = cv2.subtract(gp_orange[i-1], gp_extend)
#     lp_orange.append(laplacian)


#Add left from apple and right from orange

apple_orange_pyramid = []
n = 0

for apple_lap, orange_lap in zip(lp_apple,lp_orange):
    n +=1
    cols, rows, ch = apple_lap.shape()
    laplacian = np.hstack((apple_lap[:,:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#Reconstruct the image

apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)


cv2.imshow('apple', img1)
cv2.imshow('orange', img2)
cv2.imshow('app_org mix', app_orng)
cv2.imshow('apple_orange_reconstructed', apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()