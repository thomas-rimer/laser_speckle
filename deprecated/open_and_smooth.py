import cv2
import numpy as np
from matplotlib import pyplot as plt

def open_and_load(input_path):
    
    b_size = 21
    images = []

    # Open original image
    img_original = cv2.imread(input_path)
    if img_original is None:
        print("Error: could not identify image")
        return 
    
    cv2.imshow("Original image", img_original)

    # Convert to greyscale
    img_grey = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grey image", img_grey)
    images.append(img_grey)
    
    # Average
    avg_kernel = np.ones((b_size,b_size),np.float32)/(b_size*b_size)
    img_average = cv2.filter2D(img_grey,-1,avg_kernel)
    cv2.imshow("Average image", img_grey)
    images.append(img_average)

    # Gaussian smoothing
    img_gaussian = cv2.GaussianBlur(img_grey,(b_size,b_size), 0)
    cv2.imshow("Gaussian image", img_gaussian)
    images.append(img_gaussian)

    # Median bluring
    img_median = cv2.medianBlur(img_grey,b_size)
    cv2.imshow("Median image", img_median)
    images.append(img_median)

    # --- Identifying peaks ---
    marked_images = []
    for i in range(len(images)):
        print("Starting " + str(i))
        input_img = images[i]
        marked_image = img_original.copy()

        height, width = input_img.shape
        
        for y in range(1, height-1):
            for x in range(1, width - 1):
                center_val = input_img[y,x]

                neighbors = [
                    input_img[y-1, x-1], input_img[y-1, x], input_img[y-1, x+1],
                    input_img[y, x-1], input_img[y, x+1],
                    input_img[y+1, x-1], input_img[y+1, x], input_img[y+1, x+1],
                ]

                # Mark high point
                if all(center_val >= n for n in neighbors):
                    cv2.circle(marked_image, (x, y), 2, (255, 0, 0), -1)

        
        marked_images.append(marked_image)

    for i in range(len(marked_images)):
        cv2.imshow("img" + str(i), marked_images[i])


    cv2.waitKey()
    cv2.destroyAllWindows()
    return

if __name__ == "__main__":
    input_path = "test2.png"   # Replace with your input image path
    output_path = "output.jpg" # Replace with your desired output path
    open_and_load(input_path)




    # plt.subplot(221),plt.imshow(img_original),plt.title('Original')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(222),plt.imshow(img_average),plt.title('Averaging')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(223),plt.imshow(img_gaussian),plt.title('Gaussian')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(223),plt.imshow(img_gaussian),plt.title('Gaussian')
    # plt.xticks([]), plt.yticks([])
    # plt.show()