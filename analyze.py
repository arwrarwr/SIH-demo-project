import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

DATA_FOLDER = "DATA"

def analyze_sand_image(image_path):
    # Load greyscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return

    # Enhance contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced_img = clahe.apply(img)

    # Denoise to clean image
    denoised_img = cv2.fastNlMeansDenoising(enhanced_img, None, h=10)

    # Adaptive thresholding for segmentation
    thresh = cv2.adaptiveThreshold(
        denoised_img, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11, 2
    )

    # Find contours (grains)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out noise contours by area threshold
    valid_grains = [cnt for cnt in contours if cv2.contourArea(cnt) > 20]

    # Calculate grain areas (pixels)
    grain_areas = [cv2.contourArea(c) for c in valid_grains]

    print(f"Detected {len(valid_grains)} sand grains.")
    if len(grain_areas) > 0:
        print(f"Grain Areas (pixels, sample): {grain_areas[:10]}")

    # Visualization: draw contours on the original image
    output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_img, valid_grains, -1, (0, 255, 0), 1)

    # Plot original and segmented images side-by-side
    plt.figure(figsize=(12, 6))
    plt.subplot(1,2,1)
    plt.title("Original Grayscale Image")
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title("Segmented Sand Grains")
    plt.imshow(output_img)
    plt.axis('off')
    plt.show()

    # (Optional) Save results to a text file
    base_name = os.path.basename(image_path)
    name_without_ext = os.path.splitext(base_name)[0]
    results_file = os.path.join(DATA_FOLDER, f"{name_without_ext}_results.txt")
    with open(results_file, "w") as f:
        f.write(f"Total grains detected: {len(valid_grains)}\n")
        f.write("Grain areas (pixels):\n")
        for area in grain_areas:
            f.write(f"{area}\n")
    print(f"Results saved to {results_file}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 analyze.py <path_to_image>")
    else:
        analyze_sand_image(sys.argv[1])
