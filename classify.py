# Classify sand based on mean grain area in mm^2 or median.

def classify_beach(grain_stats, grain_area_mm2_thresholds=(0.025, 0.25)):
    # Thresholds: (typically 0.0625-2 mm diam, so approx pi*(r^2); adjust as needed)
    if grain_stats.get("grain_areas_mm2") is None:
        return "Uncalibrated: Unknown"

    mean_area = grain_stats["mean_area_mm2"]
    if mean_area < grain_area_mm2_thresholds[0]:
        return "Fine sand"
    elif mean_area < grain_area_mm2_thresholds[1]:
        return "Medium sand"
    else:
        return "Coarse sand"
