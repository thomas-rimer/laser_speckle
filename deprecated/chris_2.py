import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read the image
img = cv2.imread('test.png', cv2.IMREAD_COLOR)

# 2. Convert to grayscale on a 0–1 scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

# 3. Apply Gaussian smoothing with a 25x25 kernel
blurred = cv2.GaussianBlur(gray, (25, 25), 0)

# 4. Convolve using a 3x3 kernel
kernel_3x3 = np.ones((3, 3), dtype=np.float32) / 9.0
convolved = cv2.filter2D(blurred, -1, kernel_3x3)

# 5. Flatten the convolved image into a 1D array (all the pixel values)
pixel_values = convolved.flatten()

# 6. Plot the histogram of the convolved intensities
plt.hist(pixel_values, bins=50)  # You can choose the number of bins
plt.title("Laser Speckle Intensity Distribution")

# add a subtitle
plt.suptitle("Distrobution of pixel intensities from image captured of speckle pattern \n generated from 120 grit sanded sample", fontsize=10)


plt.xlabel("Intensity (arbitrary units, not normalized)")
plt.ylabel("Count")
plt.yscale("log")

# Compute the average intensity
avg_intensity = np.mean(pixel_values)

# Plot a vertical red line at the average intensity
#plt.axvline(x=avg_intensity, color='red', linestyle='dashed', linewidth=2)

# Optionally, add some text or a legend showing the mean value
# plt.text(avg_intensity * 1.01, plt.ylim()[1] * 0.9,
#          f"Mean = {avg_intensity:.4f}",
#          color='red')

plt.show()

