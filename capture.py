import os
from picamera import PiCamera
from time import sleep
from datetime import datetime

# Folder to save images
DATA_FOLDER = "DATA"

def ensure_data_folder():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

def get_timestamp():
    return datetime.now().strftime("%Y%m%d-%H%M%S")

def capture_image():
    ensure_data_folder()
    timestamp = get_timestamp()
    filename = f"sand_{timestamp}.jpg"
    save_path = os.path.join(DATA_FOLDER, filename)

    camera = PiCamera()
    camera.resolution = (1920, 1080)  # HD quality
    camera.framerate = 15

    # Camera enhancement settings
    camera.exposure_mode = 'auto'
    camera.shutter_speed = 0
    camera.iso = 100
    camera.awb_mode = 'auto'

    camera.start_preview()
    sleep(2)  # Allow camera to adjust lighting

    # Take multiple pictures to let camera adjust and capture stable frame
    for i in range(3):
        camera.capture(f"{DATA_FOLDER}/temp_{i}.jpg")
        sleep(0.5)

    camera.capture(save_path)
    camera.stop_preview()
    camera.close()

    print(f"Image saved at: {save_path}")
    return save_path, timestamp

def main():
    # Capture image and save with timestamped name in DATA folder
    image_path, timestamp = capture_image()

    # GPS integration code commented out for future use
    """
    import gpsd
    gpsd.connect()
    packet = gpsd.get_current()
    lat = packet.lat
    lon = packet.lon
    print(f"GPS Coordinates: Latitude={lat}, Longitude={lon}")
    gps_filename = os.path.join(DATA_FOLDER, f"sand_{timestamp}_gps.txt")
    with open(gps_filename, "w") as f:
        f.write(f"{lat},{lon}\n")
    """

    print("GPS module not connected, skipped GPS capture.")

if __name__ == "__main__":
    main()
