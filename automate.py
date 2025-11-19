from gpiozero import Button
import subprocess

button = Button(18)  # GPIO pin

def main_work():
    subprocess.call(['python3', '/home/pi/sand/sand_grain_mapping/main.py'])
    print("Script run once - exiting program")
    exit(0)  # End this GPIO listener program after running once

button.when_pressed = main_work

# Wait forever or until exit()
button.wait_for_press()
