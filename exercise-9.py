import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('flor.jpg')

img_orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, otsu_img = cv2.threshold(gray, 127, 255, cv2.THRESH_OTSU)
ret, trunc_img = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret, zero_img = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)

plt.subplot(321),plt.imshow(gray, cmap="gray"),plt.title('Gray')
plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(otsu_img, cmap="gray"),plt.title('Otsu tresholded')
plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(trunc_img, cmap="gray"),plt.title('Trunc tresholded')
plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(zero_img, cmap="gray"),plt.title('To zero tresholded')
plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(img_orig),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.show()