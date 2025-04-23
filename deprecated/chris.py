import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read the image
# Replace 'your_image.jpg' with your actual image filename/path.
img = cv2.imread('test.png', cv2.IMREAD_COLOR)

# 2. Convert to grayscale on a 0–1 scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

# 3. Apply Gaussian smoothing with a 25x25 kernel
blurred = cv2.GaussianBlur(gray, (25, 25), 0)

# 4. Convolve using a 3x3 kernel
#    Here we use a simple averaging kernel of size 3x3.
kernel_3x3 = np.ones((3, 3), dtype=np.float32) / 9.0
convolved = cv2.filter2D(blurred, -1, kernel_3x3)

# 5. Flatten the convolved image into a 1D array (all the pixel values)
pixel_values = convolved.flatten()

# 6. Plot the histogram of the convolved intensities
plt.hist(pixel_values, bins=50)  # You can choose the number of bins
plt.title("Histogram of Convolved Intensities")
plt.xlabel("Intensity")
plt.ylabel("Count")
plt.show()