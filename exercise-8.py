import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('choc.png')

img_orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, bin_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

blur_img = cv2.blur(bin_img, (5, 5))
can_img = cv2.Canny(bin_img, 586, 388)

plt.subplot(321),plt.imshow(img_orig),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(gray, cmap="gray"),plt.title('Gray')
plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(bin_img, cmap="gray"),plt.title('Binary')
plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(blur_img, cmap="gray"),plt.title('Blur filter')
plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(can_img, cmap="gray"),plt.title('Canny filter')
plt.xticks([]), plt.yticks([])
plt.show()