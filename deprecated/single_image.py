import cv2
import numpy as np

def mark_local_bright_spots(input_image_path, output_image_path):
    
    # Import original image
    img_original = cv2.imread(input_image_path)
    if img_original is None:
        print("Error: Could not load the image.")
        return
    
    # Convert to gray
    img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

    # Blur image to remove high frequency noise
    img_blur = cv2.blur(img_gray, [20,20])
    
    cv2.imshow("img_blur", img_blur)

    print(

    
    """ if points is None:
        print("No local bright spots found.")
    else:
        # 4. Mark these points on the color image
        for p in points:
            x, y = p[0]
            # Draw a small red circle on each local max
            cv2.circle(img_color, (x, y), 2, (0, 0, 255), -1)

    # 5. Save or display the result
    cv2.imwrite(output_image_path, img_color)
    print(f"Output saved to {output_image_path}") """

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_path = "test.png"   # Replace with your input image path
    output_path = "output.jpg" # Replace with your desired output path
    mark_local_bright_spots(input_path, output_path)