import cv2
import numpy as np
import matplotlib.pyplot as plt

# Open the raw image file
img_raw = rawpy.imread('phys_2210_photos/control_grit/IMG_4967.CR2')
img_rgb = img_raw.postprocess(no_auto_bright=True, output_bps=16) #img_raw.postprocess(no_auto_bright=True, output_bps=16)


print("img_rgb: ")
print("shape:", img_rgb.shape)
print("dtype:", img_rgb.dtype)
print("min:", np.min(img_rgb))
print("max:", np.max(img_rgb))
print(img_rgb[:, 0, 1])
cv2.imshow("img_rgb", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''

img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)

# Apply Gaussian smoothing with a 25x25 kernel
#img_blurred = cv2.GaussianBlur(img_gray, (25, 25), 0)
img_blurred = img_gray

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

'''