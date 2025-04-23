import rawpy
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Define the directory path
directory = 'phys_2210_photos/150_grit'

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.startswith('IMG_') and filename.endswith('.CR2'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Open the raw image file
        img_raw = rawpy.imread(file_path)
        img_rgb = img_raw.postprocess()
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

        # Apply Gaussian smoothing with a 25x25 kernel
        img_blurred = cv2.GaussianBlur(img_gray, (25, 25), 0)

        # Convolve using a 3x3 kernel
        kernel_3x3 = np.ones((3, 3), dtype=np.float32) / 9.0
        img_convolved = cv2.filter2D(img_blurred, -1, kernel_3x3)

        # Flatten the convolved image into a 1D array (all the pixel values)
        pixel_values = img_convolved.flatten()

        # Plot the histogram of the convolved intensities
        plt.hist(pixel_values, bins=50)
        plt.title("Laser Speckle Intensity Distribution")
        plt.xlabel("Intensity (arbitrary units, not normalized)")
        plt.ylabel("Count")
        plt.yscale("log")

        plt.show()