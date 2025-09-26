from capture import capture_image, get_timestamp
from analyze import analyze_sand_image

def main():
    print("Starting image capture...")
    # Capture image and receive path and timestamp
    image_path, timestamp = capture_image()

    print("Starting sand grain size analysis...")
    # Analyze captured image
    analyze_sand_image(image_path)

    print("Process completed.")

if __name__ == "__main__":
    main()


# okhey so just do this, run the file 
# it will - capture an image with camera and save it in DATA folder and then run the analysis on the image and then you should see printed grain count, area outputs, segmentation visualization pop up
