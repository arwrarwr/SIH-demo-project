import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from utils import calibrate_pixel_to_mm

DATA_FOLDER = "DATA"

def analyze_sand_image(image_path, scale_mm_per_pixel=None, show_viz=True):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None

    # Contrast improvement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced_img = clahe.apply(img)

    # Denoising
    denoised_img = cv2.fastNlMeansDenoising(enhanced_img, None, h=10)

    # Thresholding (segmentation)
    thresh = cv2.adaptiveThreshold(
        denoised_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    valid_grains = [cnt for cnt in contours if cv2.contourArea(cnt) > 20]
    grain_areas_pix = [cv2.contourArea(c) for c in valid_grains]

    # Convert to mm^2 if scale available
    if scale_mm_per_pixel is not None:
        grain_areas_mm2 = [a * (scale_mm_per_pixel**2) for a in grain_areas_pix]
    else:
        grain_areas_mm2 = None

    # Stats
    grain_stats = {
        "grain_count": len(valid_grains),
        "grain_areas_pix": grain_areas_pix,
        "grain_areas_mm2": grain_areas_mm2,
        "mean_area_pix": np.mean(grain_areas_pix) if grain_areas_pix else 0,
        "median_area_pix": np.median(grain_areas_pix) if grain_areas_pix else 0,
        "max_area_pix": np.max(grain_areas_pix) if grain_areas_pix else 0,
        "min_area_pix": np.min(grain_areas_pix) if grain_areas_pix else 0,
    }
    if grain_areas_mm2:
        grain_stats["mean_area_mm2"] = np.mean(grain_areas_mm2)
        grain_stats["median_area_mm2"] = np.median(grain_areas_mm2)

    output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_img, valid_grains, -1, (0, 255, 0), 1)

    if show_viz:
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

    # Return stats and list of valid grain contours for further use
    return grain_stats

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 analyze.py <path_to_image>")
    else:
        analyze_sand_image(sys.argv[1])

