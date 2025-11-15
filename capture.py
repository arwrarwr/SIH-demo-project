import os
from picamera2 import Picamera2, Preview
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

    camera = Picamera2()
    camera_config = camera.create_preview_configuration({"size":(1920, 1080)})
    capture_config = camera.create_still_configuration({"size": (1920, 1080)})
    camera.configure(camera_config)
    camera.configure(capture_config)

    camera.start_preview(Preview.QTGL)
    camera.start()
    sleep(2)

    # Take multiple pictures to let camera adjust and capture stable frame
    '''for i in range(3):
        camera.capture_file(f"{DATA_FOLDER}/temp_{i}.jpg")
        sleep(0.5)'''

    camera.capture_file(save_path)

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
