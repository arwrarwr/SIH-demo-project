import os
import cv2
from datetime import datetime

DATA_FOLDER = "DATA"

def ensure_data_folder():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

def get_timestamp():
    return datetime.now().strftime('%Y%m%d_%H%M%S')

def capture_image():
    ensure_data_folder()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera not accessible")
        return None, None
    ret, frame = cap.read()
    if ret:
        timestamp = get_timestamp()
        image_path = os.path.join(DATA_FOLDER, f"sand_sample_{timestamp}.jpg")
        cv2.imwrite(image_path, frame)
        print(f"Image captured: {image_path}")
        cap.release()
        return image_path, timestamp
    else:
        print("Failed to capture image.")
        cap.release()
        return None, None

