import os
import cv2
import numpy as np

def crop_black_borders(image):
    """
    Automatically detects and removes black borders, even if they are not pure black.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Handle transparency by converting alpha to white background
    if image.shape[-1] == 4:  
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    # Adaptive thresholding to detect dark borders
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)  

    # Get non-black coordinates
    mask = gray < 20  # Treats anything darker than 20 as black
    coords = np.column_stack(np.where(~mask))

    if coords.shape[0] == 0:
        print("No content found in image, returning original.")
        return image  # If no content detected, return original image

    # Get bounding box
    x_min, y_min = coords.min(axis=0)
    x_max, y_max = coords.max(axis=0)

    # Prevent cropping if borders were not found
    if x_min == 0 and y_min == 0 and x_max == image.shape[0] - 1 and y_max == image.shape[1] - 1:
        print("No borders detected, skipping...")
        return image

    # Expand crop slightly to remove remaining thin lines
    padding = 2
    cropped_image = image[max(0, x_min - padding): min(image.shape[0], x_max + padding),
                          max(0, y_min - padding): min(image.shape[1], y_max + padding)]

    return cropped_image

def process_images(input_folder, output_folder):
    """
    Processes all .webp images in the input folder and saves cropped images in the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".webp"):
            img_path = os.path.join(input_folder, filename)
            image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)  # Read with alpha channel if present

            if image is None:
                print(f"Skipping {filename}, unable to load image.")
                continue

            cropped_image = crop_black_borders(image)

            # Save the cropped image
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, cropped_image)
            print(f"Cropped and saved: {output_path}")

# Set folder paths
input_folder = "cards"   # Folder containing original images
output_folder = "output_images" # Folder to save cropped images

process_images(input_folder, output_folder)

