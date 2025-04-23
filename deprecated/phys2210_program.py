import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

grits = [] # integer values representing the grits. corrosponds to each row of distributions
distributions = [] # x: grit, y: sample #, z: distribution

def produce_distro(image_name):
    # Read the image
    img = cv2.imread(image_name, cv2.IMREAD_COLOR)
    if img is None:
        print(f"Error: Unable to read image {image_name}")
        return

    # Convert to grayscale on a 0–1 scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0

    # Apply Gaussian smoothing with a 25x25 kernel
    blurred = cv2.GaussianBlur(gray, (25, 25), 0)

    # Convolve using a 3x3 kernel
    kernel_3x3 = np.ones((3, 3), dtype=np.float32) / 9.0
    convolved = cv2.filter2D(blurred, -1, kernel_3x3)
    
    # Flatten the convolved image into a 1D array (all the pixel values)
    pixel_values = convolved.flatten()

# For each folder (grit)
for folder in os.listdir('.'):
    if os.path.isdir(folder):
        grits.append(folder)
        
        # For each sample of a given grit (1 - 10)
        for image_name in os.listdir(folder):
            if image_name.endswith('.png'):
                produce_distro(os.path.join(folder, image_name))
            else:
                print(f"Skipping {image_name} as it is not a .png file")