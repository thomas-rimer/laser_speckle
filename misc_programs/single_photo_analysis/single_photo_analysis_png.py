import rawpy
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Open the raw image file
img_import = cv2.imgread('phys_2210_photos/control_grit/IMG_4967.png')
img_gray = cv2.cvtColor(img_import, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

# Apply Gaussian smoothing with a 25x25 kernel
#img_blurred = cv2.GaussianBlur(img_gray, (25, 25), 0)
img_blurred = img_gray

# Print min, max, and average value of img_blurred
print("blurred type:", type(img_blurred))
print("blurred shape:", img_blurred.shape)
print(img_blurred)
print("blurred image min value:", np.min(img_blurred))
print("blurred image max value:", np.max(img_blurred))
print("blurred image average value:", np.mean(img_blurred))

# Convolve using a 3x3 kernel
kernel_3x3 = np.ones((3, 3), dtype=np.float32) / 9.0
img_convolved = cv2.filter2D(img_blurred, -1, kernel_3x3)

# Flatten the convolved image into a 1D array (all the pixel values)
pixel_values = img_convolved.flatten()

# --- Background ---

# Open the background_reference image
background_reference = rawpy.imread('phys_2210_photos/control_grit/control_background.CR2')
background_rgb = background_reference.postprocess(no_auto_bright=True, output_bps=16)
#background_bgr = cv2.cvtColor(background_rgb, cv2.COLOR_RGB2BGR)
#background_gray = cv2.cvtColor(background_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

# Print min, max, and average value of background_rgb
print("rgb type:", type(background_rgb))
print("shape:", background_rgb.shape)
print(background_rgb)
print("Background image min value:", np.min(background_rgb))
print("Background image max value:", np.max(background_rgb))
print("Background image average value:", np.mean(background_rgb))

# show the background image
cv2.imshow("background", background_reference)

# --- Show the images ---

# Subtract the background from the convolved image
pixel_values = pixel_values - background_avg

# Normalize
pixel_values = pixel_values / np.max(pixel_values)

# Plot the histogram of the convolved intensities
plt.hist(pixel_values, bins=50)
plt.title("Laser Speckle Intensity Distribution")
plt.xlabel("Intensity (arbitrary units, normalized against brighest spot)")
plt.ylabel("Count")
plt.yscale("log")

plt.show()