import matplotlib.pyplot as plt
import datetime
import numpy as np

slopes = np.array([-12.536, -15.709, -11.434, -8.777, -9.680, -9.059, -10.240, -6.184, -7.896, -8.141, -9.049])
slopes = slopes*-1
grits = [150, 180, 240, 320, 400, 600, 800, 1000, 1500, 2500, 3000]

plt.figure(figsize=(10, 6))
plt.plot(grits, slopes, marker='o', linestyle='-', color='red')
plt.title('Slope of Exponential Fit Based on Grit')
plt.xlabel('Grit Size (grit)')
plt.ylabel('Slope of Exponential Fits to Histogram for Each Grit')
plt.grid()
# avoid the x-ticks overlapping
plt.xticks([150, 180, 240, 320, 400, 600, 800, 1000, 1500, 2500, 3000], ['150', '', '240', '320', '400', '600', '800', '1000', '1500', '2500', '3000'], rotation=90)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = "outputs"
output_filename = f"slope_trend{timestamp}.png"
output_path = f"{output_dir}/{output_filename}"
plt.savefig(output_path, dpi=600)
plt.show()