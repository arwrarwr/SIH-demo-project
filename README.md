#instructions 
# Sand Grain Size Mapping Project

## Overview
This project develops a low-cost, automated solution to estimate sand grain size distribution using a Raspberry Pi 4, Pi Camera Module, and image analysis techniques. The system captures clear images of sandy beach areas, processes those images to segment and measure grain sizes, and outputs detailed size statistics with visualization. GPS integration is planned for geotagging sample locations.

This tool aids coastal scientists and researchers by reducing the need for labor-intensive sediment sampling and lab processing.

---

## Features
- High quality image capture optimized for Raspberry Pi Camera Module
- Adaptive image preprocessing and segmentation to isolate sand grains
- Automated calculation of grain size areas from segmented images
- Visualization of segmentation results
- Modular scripts supporting extensibility (e.g., GPS integration)
- Organized data storage with timestamped images and analysis outputs

---

## Hardware Requirements
- Raspberry Pi 4 with Raspberry Pi OS installed
- Raspberry Pi Camera Module (CSI interface)
- (Optional) GPS module for geolocation data

---

## Software Setup

### Dependencies
Install required Python libraries:

pip3 install -r requirements.txt

text
Required packages include:
- `picamera`
- `opencv-python`
- `numpy`
- `matplotlib`
- `Pillow`

### Enable Camera Interface
Enable the camera on your Raspberry Pi:

sudo raspi-config
Navigate: Interface Options > Camera > Enable

text
Reboot if prompted.

---

## File Structure

SAND GRAIN/
├── DATA/ # Stores captured images and results
├── analyze.py # Grain size analysis script
├── capture.py # Image capture script
├── main.py # Orchestrates capture + analysis
├── gps_coords.txt # GPS data storage (future use)
├── README.md # This file
├── requirements.txt # Library dependencies
├── sand_sample.jpg # Sample image for offline testing

text

---

## How to Run

### Step 1: Capture Image
Run this to capture a high-quality image with your Pi camera:

python3 capture.py

text
Image saved in `DATA/` folder with timestamp.

### Step 2: Analyze Image
Analyze a specific image (use captured or sample image):

python3 analyze.py DATA/sand_YYYYMMDD-HHmmss.jpg

text
Outputs grain count and size stats, plus visualization.

### Step 3: Full Pipeline
Run the combined workflow that captures and analyzes automatically:

python3 main.py

text

---

## Troubleshooting & Tips

- **Blurry or Dark Images:**  
  - Ensure good lighting, avoid camera shake.  
  - Allow camera preview time before capture for exposure adjustment.  
  - Try adjusting camera settings in `capture.py` (e.g., ISO, shutter speed).

- **Library Installation Issues:**  
  - Upgrade `pip`: `pip3 install --upgrade pip`  
  - Install required packages individually.

- **Camera Not Detected:**  
  - Verify camera is enabled in `raspi-config`.  
  - Check cable is securely connected.

- **Image Analysis Errors:**  
  - Verify image path is correct.  
  - Test `analyze.py` with provided `sand_sample.jpg` first.  
  - Tune contour area threshold for noise filtering in `analyze.py`.

- **GPS Module Not Available Yet:**  
  - GPS integration is optional and commented out in scripts.  
  - When available, uncomment GPS parts and install `gpsd-py3`.

---

## Future Work

- Integrate GPS module for precise location tagging.  
- Improve segmentation using deep learning (CNNs) for complex cases.  
- Add mapping visualization (e.g., folium) with geotagged sample points.  
- Implement batch processing for larger datasets.  

---

## Acknowledgments

Special thanks to the Raspberry Pi Foundation for the hardware platform and to the open-source community providing excellent Python libraries enabling this project.

---

## License

Specify your license here (e.g., MIT License).

---

*For questions or collaboration opportunities, contact [Your Contact Info].*