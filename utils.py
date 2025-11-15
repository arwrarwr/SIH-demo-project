import cv2
import numpy as np

def calibrate_pixel_to_mm(image_path=None, marker_mm=24.0):
    """
    Manual scale calibration: user should photograph a known marker (e.g., 10mm coin)
    Returns mm_per_pixel or None if calibration image not provided.
    """
    if image_path is None:
        return None

    img = cv2.imread(image_path)
    if img is None:
        return None

    # [TODO] Replace manual ROI/marker detection with OpenCV circle detection or ask user for pixel length
    # For demo, ask user to input the pixel length of the marker in the image
    print("Open your calibration image and measure the marker in pixels using image editor.")
    marker_pixels = float(input("Enter measured marker diameter (pixels): "))
    mm_per_pixel = marker_mm / marker_pixels
    return mm_per_pixel
