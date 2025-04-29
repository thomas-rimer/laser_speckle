# import png image with opencv
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ingest image
img_import = cv2.imread('phys_2210_photos/150_grit/IMG_4837.png', cv2.IMREAD_UNCHANGED)
img_gray = cv2.cvtColor(img_import, cv2.COLOR_BGR2GRAY)

# Ingest background reference image
img_background = cv2.imread('phys_2210_photos/150_grit/150_background.png', cv2.IMREAD_UNCHANGED)
img_background = cv2.cvtColor(img_background, cv2.COLOR_BGR2GRAY)
background_avg_un_normalized = np.mean(img_background)

# Subtract the background from the image
img_gray = img_gray - background_avg_un_normalized

# Smooth the image
img_blurred = img_gray #cv2.GaussianBlur(img_gray, (25, 25), 0)

# Convolve image
kernel_3x3 = np.ones((3, 3), dtype=np.float32) / 9.0
img_convolved = cv2.filter2D(img_blurred, -1, kernel_3x3)

# Normalize and extract individual pixel values
pixel_values = img_convolved.flatten()
pixel_values_norm = pixel_values / (np.float64(2**16) - background_avg_un_normalized)

print("Pixel values statistics:")
print("shape:", pixel_values.shape)
print("dtype:", pixel_values.dtype)
print("min:", np.min(pixel_values_norm))
print("max:", np.max(pixel_values_norm))
print("mean:", np.mean(pixel_values_norm))
print("std:", np.std(pixel_values_norm))
print("median:", np.median(pixel_values_norm))

# Generate histogram
plt.hist(pixel_values_norm, bins=50)
plt.title("Laser Speckle Intensity Distribution")
plt.xlabel("Intensity (arbitrary units, normalized against sensor)")
plt.ylabel("Count")
plt.xlim(0, 1)
plt.yscale('log')
plt.ylim(10, 1e8)


plt.grid()
plt.show()
