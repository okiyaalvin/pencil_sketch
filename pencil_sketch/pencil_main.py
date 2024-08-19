import cv2
import numpy as np
import os


def pencil_sketch(image_path, output_path):
    print("Loading image...")
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found or unable to load.")
        return
    print("Image loaded successfully.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Converted to grayscale.")

    inverted_gray_image = cv2.bitwise_not(gray_image)
    print("Inverted grayscale image.")

    blurred_image = cv2.GaussianBlur(inverted_gray_image, (7, 7), 0)
    print("Applied Gaussian blur.")

    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    print("Inverted blurred image.")

    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    print("Created pencil sketch image.")

    cv2.imwrite(output_path, pencil_sketch_image)
    print(f"Output saved to {output_path}.")

    cv2.imshow('Pencil Sketch', pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Display current working directory
print("Current Working Directory:", os.getcwd())

# Prompt the user to enter the image path and clean up any surrounding quotes
input_image_path = input("Please enter the path to the image: ").strip('"')
output_image_path = 'w2_sketch.jpg'  # You can set a specific output path here

pencil_sketch(input_image_path, output_image_path)
