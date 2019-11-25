import cv2

img = cv2.imread('lena.jpg')
layer = img.copy()
gp = []

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

#LAPLACIAN PRYAMID
layer = gp[4]
lp = [layer]

for i in range(4, 0, -1):
    gaussian_extnd = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extnd)
    cv2.imshow(str(i), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()


