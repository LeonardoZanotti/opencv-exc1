import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('flor.jpg')

img_orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gau_img = cv2.GaussianBlur(gray, (5, 5), 0)
ret1, gau_bin_img = cv2.threshold(gau_img, 127, 255, cv2.THRESH_BINARY)
ret2, gray_bin_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

plt.subplot(321),plt.imshow(gray, cmap="gray"),plt.title('Gray')
plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(gau_img, cmap="gray"),plt.title('Gaussian Filter')
plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(gray_bin_img, cmap="gray"),plt.title('Gray tresholded')
plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(gau_bin_img, cmap="gray"),plt.title('Gaussian filter tresholded')
plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(img_orig),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.show()