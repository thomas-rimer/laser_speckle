import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from pathlib import Path
import re
import datetime

ROUND = 2

def linear_fit(x, a, b):
    return a * x + b

list_of_grits = [0, 150, 180, 240, 320, 400, 600, 800, 1000, 1500, 2500, 3000]
all_slopes = []
slope_uncertainties = []

for current_grit in list_of_grits:

    GRIT = current_grit

    # Ingest background reference image
    img_background = cv2.imread('phys_2210_photos/' + str(GRIT) + '_grit/' + str(GRIT) + '_background.png', cv2.IMREAD_UNCHANGED)
    img_background = cv2.cvtColor(img_background, cv2.COLOR_BGR2GRAY)
    background_avg_un_normalized = np.mean(img_background)

    # Grit wide arrays
    grit_bin_values = []
    grit_bin_centers = []
    grit_slopes = []
    grit_intercepts = []
    grit_uncertainties = []

    # Directory information
    GRIT_DIR = Path(r"phys_2210_photos/" + str(GRIT) + "_grit").expanduser().resolve()
    NAME_PATTERN = re.compile(r"^IMG_\d{4}\.png$", re.IGNORECASE)

    for file in sorted(GRIT_DIR.iterdir()):
        if file.is_file() and NAME_PATTERN.fullmatch(file.name):
            image_path = str(file)
            print(image_path) 

            # Ingest image
            img_import = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
            img_gray = cv2.cvtColor(img_import, cv2.COLOR_BGR2GRAY)

            # Subtract the background from the image
            img_gray = img_gray - background_avg_un_normalized

            # Smooth the image
            img_blurred = cv2.GaussianBlur(img_gray, (25, 25), 0)

            # Convolve image
            kernel_3x3 = np.ones((3, 3), dtype=np.float32) / 9.0
            img_convolved = cv2.filter2D(img_blurred, -1, kernel_3x3)

            # Normalize and extract individual pixel values
            pixel_values = img_convolved.flatten()
            pixel_values_norm = pixel_values / (np.float64(2**16) - background_avg_un_normalized)

            # Generate histogram bins
            bin_values, bin_edges = np.histogram(pixel_values_norm, bins=np.linspace(0, 1, 101))
            bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
            grit_bin_values.append(bin_values)
            grit_bin_centers.append(bin_centers)

            # Isolate bins for fitting
            max_bin_index = np.argmax(bin_values)
            max_bin_value = bin_centers[max_bin_index]
            fit_bin_centers = bin_centers[max_bin_index + 1:max_bin_index + 10]
            fit_bin_values = bin_values[max_bin_index + 1:max_bin_index + 10]

            # Line of best fit to isolated bins
            fit_bin_values_log = np.log10(fit_bin_values + 1e-10)  # Adding a small constant to avoid log(0)
            params, covariance = curve_fit(linear_fit, fit_bin_centers, fit_bin_values_log)
            slope, intercept = params
            print("Fitted parameters:")
            print("Slope:", slope)
            print("Intercept:", intercept)

            grit_slopes.append(slope)
            grit_intercepts.append(intercept)
            grit_uncertainties.append(covariance[0,0])

            print(" ")
            print(" ")
            print(" ")

    # --- Fit #1: Recalculate New Fit based on Average Histogram ---

    # Average the grit bins (centers and values) across all images
    grit_bin_values = np.array(grit_bin_values)
    grit_bin_centers = np.array(grit_bin_centers)
    average_grit_bin_centers = np.mean(grit_bin_centers, axis=0)

    average_grit_bin_values = np.mean(grit_bin_values, axis=0)
    std_grit_bin_values = np.std(grit_bin_values, axis=0)

    # Isolate average bins for fitting
    max_grit_bin_index = np.argmax(average_grit_bin_values)
    max_grit_bin_value = average_grit_bin_centers[max_grit_bin_index]
    average_fit_bin_centers = average_grit_bin_centers[max_grit_bin_index + 1:max_grit_bin_index + 10]
    average_fit_bin_values = average_grit_bin_values[max_grit_bin_index + 1:max_grit_bin_index + 10]

    # Line of best fit for to isolated bins
    grit_bin_values_log = np.log10(average_fit_bin_values + 1e-10) # small constant offset added to avoid log(0)
    grit_params, grit_covariance = curve_fit(linear_fit, average_fit_bin_centers, grit_bin_values_log)
    extracted_grit_slope, extracted_grit_intercept = grit_params
    print("Average Fitted parameters:")
    print("Slope:", extracted_grit_slope)
    print("Intercept:", extracted_grit_intercept)

    # --- Fit #2: Average Existing Slopes, no new fitting --- 
    existing_slopes_average = np.mean(grit_slopes)
    existing_intercepts_average = np.mean(grit_intercepts)
    
    # UNCERTAINTY
    error_propogated_uncertainty = 1.0/10.0 * np.sqrt(np.sum(grit_uncertainties))
    slope_uncertainties.append(error_propogated_uncertainty)

    #Plot histrogram
    plt.figure(figsize=(10, 6))
    plt.bar(average_grit_bin_centers, average_grit_bin_values, width=bin_edges[1] - bin_edges[0], color='red', alpha=0.7, edgecolor='black')
    plt.errorbar(average_grit_bin_centers, average_grit_bin_values, yerr=std_grit_bin_values, fmt='none', ecolor='black', capsize=5, label='Standard Deviation')
    plt.plot(average_grit_bin_centers, 10**(linear_fit(average_grit_bin_centers, *grit_params)), color='blue', label=f'Exponential fit (slope={extracted_grit_slope:.3f}, intercept={extracted_grit_intercept:.3f})')
    #plt.plot(average_grit_bin_centers, 10**(linear_fit(average_grit_bin_centers, *(existing_slopes_average, existing_intercepts_average))), color='yellow', linestyle='--', label='Approach #2: Average existing')
    plt.title("Laser Speckle Intensity Distribution: " + str(GRIT) + " Grit")
    plt.xlabel("Intensity (arbitrary units, normalized against sensor)")
    plt.ylabel("Count")
    plt.xlim(0, 1)
    plt.yscale('log')
    plt.ylim(10, 1e8)
    plt.legend()

    plt.grid()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = "outputs/round_" + str(ROUND)
    output_filename = "r" + str(ROUND) + "_" + str(GRIT) + ".png"
    output_path = f"{output_dir}/{output_filename}"

    plt.savefig(output_path, dpi=600)

    all_slopes.append(extracted_grit_slope)

list_of_grits_str = grits = ['150', '180', '240', '320', '400', '600', '800', '1000', '1500', '2500', '3000']

plt.figure(figsize=(10, 6))
plt.plot(list_of_grits[1:], (-1)*np.array(all_slopes[1:]), marker='o', linestyle='-', color='red')
plt.title('Slope of Exponential Fit Based on Grit')
plt.xlabel('Grit Size (grit)')
plt.ylabel('Slope (arbitrary units)')
plt.grid()
plt.xticks([150, 180, 240, 320, 400, 600, 800, 1000, 1500, 2500, 3000], ['150', '', '240', '320', '400', '600', '800', '1000', '1500', '2500', '3000'], rotation=90)
# plot uncertainty
plt.errorbar(list_of_grits[1:], (all_slopes[1:], yerr=slope_uncertainties[1:], fmt='o', color='black', capsize=5)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = "outputs/round_" + str(ROUND)
output_filename = "r" + str(ROUND) + "_slope_trend.png"
output_path = f"{output_dir}/{output_filename}"
plt.savefig(output_path, dpi=600)
plt.show()