import cv2

# opencv image
img_rgb = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_COLOR)
img_gray = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('RGB')
cv2.namedWindow('GRAY')
cv2.imshow('RGB', img_rgb)
cv2.imshow('GRAY', img_gray)
cv2.waitKey(5000)
cv2.destroyAllWindows()
