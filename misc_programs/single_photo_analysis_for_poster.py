import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Ingest image
img_import = cv2.imread('phys_2210_photos/2500_grit/IMG_4950.png', cv2.IMREAD_UNCHANGED)
img_gray = cv2.cvtColor(img_import, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image', img_gray)

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

# Generate histogram bins
bin_values, bin_edges = np.histogram(pixel_values_norm, bins=np.linspace(0, 1, 101))
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])

# Extract the 10 bins to the right of the maximum bin
max_bin_index = np.argmax(bin_values)
max_bin_value = bin_centers[max_bin_index]
fit_bin_centers = bin_centers[max_bin_index:max_bin_index + 10]
fit_bin_values = bin_values[max_bin_index:max_bin_index + 10]

# Take logarithm of each entry in fit_bin_values
fit_bin_values_log = np.log10(fit_bin_values + 1e-10)  # Adding a small constant to avoid log(0)
# Define a linear function for fitting
def linear_fit(x, a, b):
    return a * x + b
# Fit the linear function to the log-transformed bin values
params, covariance = curve_fit(linear_fit, fit_bin_centers, fit_bin_values_log)
# Extract the slope and intercept from the fitted parameters
slope, intercept = params
print("Fitted parameters:")
print("Slope:", slope)
print("Intercept:", intercept)

#Plot histrogram
plt.figure(figsize=(10, 6))
plt.bar(bin_centers, bin_values, width=bin_edges[1] - bin_edges[0], color='red', alpha=0.7, edgecolor='black')
plt.title("Intensity Distribution for 2500 Grit, Photo #7")
plt.xlabel("Intensity (arbitrary units, normalized against sensor)")
plt.ylabel("Count")
plt.xlim(0, 1)
plt.yscale('log')
plt.ylim(10, 1e8)
#plt.axvline(max_bin_value, color='green', linestyle='--', label='Max Bin Value')

# Plot the linear fit, but raise y values by power of 10 so it shows up as a straight line on the log y axis
#plt.plot(bin_centers, 10**(linear_fit(bin_centers, *params)), color='red', label='Linear Fit')

plt.grid()

output_dir = "outputs/round_3"
output_filename = "a2"
output_path = f"{output_dir}/{output_filename}"
plt.savefig(output_path, dpi=600)
plt.show()