now the code includes modular scripts for image capture, sand grain analysis, scale calibration, beach classification, and GPS (placeholder) 
--- should be enough for SIH problem statement 
further work would be of hardware integration and testing. 
it should start working, i made changes to almost all the files, including capture.py, to makee some directory changes, but if somehow the code breaks. 
feel free to edit it to get the hardware working. 


capture.py
    Ensures the data folder exists before saving images.
    Captures images from the camera with error checks.
    Saves images with timestamped filenames.
    Returns the image path and capture time.

analyze.py
    Loads grayscale image and improves contrast.
    Removes noise and segments sand grains.
    Finds contours and filters small noise.
    Calculates grain areas in pixels (and mm² if calibrated).
    Shows original and segmented images side-by-side.
    Returns grain size statistics.

classify.py
    Classifies beach type (fine, medium, coarse sand) based on grain size statistics in mm².
    Handles uncalibrated cases by returning “Unknown”.
gps_module.py
    Placeholder for GPS functionality.
    Returns None for coordinates until hardware is integrated.

utils.py
    Handles pixel-to-millimeter conversion based on calibration image.
    Requests manual input of the size of a known reference object in pixels.

main.py
    Manages workflow: calibration, image capture, analysis, classification, and saving results.
    Reads GPS data if available, else sets it to None.
    Saves all data and metadata in a JSON file for traceability.
 my part ? done i guess. 
