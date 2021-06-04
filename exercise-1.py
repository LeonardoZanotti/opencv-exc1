import cv2

img_gray = cv2.imread('choc.png', cv2.IMREAD_GRAYSCALE)
# img_gray[0:100, 0:100] = 0

for x in range(int(len(img_gray) / 2)):
    for y in range(len(img_gray[x])):
        img_gray[x, y] = 255 - img_gray[x, y]

cv2.namedWindow('GRAY')
cv2.imshow('GRAY', img_gray)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('./gray-choc.png', img_gray)
