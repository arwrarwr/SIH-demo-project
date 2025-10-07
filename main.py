from capture import capture_image, get_timestamp
from analyze import analyze_sand_image
from classify import classify_beach
from gps_module import get_gps_coords
from utils import calibrate_pixel_to_mm
import json
import os

DATA_FOLDER = "DATA"

def main():
    print("Optional: Calibrate scale first for accurate size estimation.")
    calibration_image = input("Enter calibration image path, or leave blank to skip: ").strip()
    scale_mm_per_pixel = None
    if calibration_image:
        scale_mm_per_pixel = calibrate_pixel_to_mm(calibration_image)
        print(f"Scale calibrated: {scale_mm_per_pixel:.5f} mm/pixel")
    else:
        print("No scale calibration. Physical sizes will not be computed.")

    print("Starting image capture...")
    image_path, timestamp = capture_image()

    print("Analyzing sand grain size...")
    grain_stats = analyze_sand_image(image_path, scale_mm_per_pixel=scale_mm_per_pixel, show_viz=True)

    # Classify sand
    sand_class = classify_beach(grain_stats)
    print(f"Sand Class: {sand_class}")

    # GNSS/GPS coords
    gps_coords = (None, None)
    try:
        # If GPS hardware not present, will return None
        gps_coords = get_gps_coords()
    except Exception as e:
        print("GPS Error:", e)

    # Save result JSON with all metadata
    meta = {
        "timestamp": timestamp,
        "image_path": image_path,
        "gps_coords": gps_coords,
        "grain_stats": grain_stats,
        "sand_classification": sand_class
    }
    output_file = os.path.join(DATA_FOLDER, f"sand_grains_{timestamp}_meta.json")
    with open(output_file, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"Full metadata saved to {output_file}")

if __name__ == "__main__":
    main()

