# The goal of this program is to explain the impact of Guassian Blurring on the final plot

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.png', cv2.IMREAD_COLOR)

# display the original image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Example Image")

# Convert to grayscale on a 0–1 scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

blur_levels = []