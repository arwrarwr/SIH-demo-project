### demo-video-code

this is just some modifications made to the duh branch. What are those
changes?

---

### changes

- program now uses picamera2 instead of opencv
- stuff that analyze function returned to main, now just prints it
- analyze imports classification data from classify, and prints it
- size of reference was hardcoded to 10, now to 24 (should be variable)
- code has the scale (mm/pixel) hardcoded, which the user should be
prompted to enter, fk that even better, will make a script that automatically
finds the reference and calcs the scale.

these changes were mostly for demo purposes, except for the picamera2 module inclusion.

---

### automation

the script is now automated, that is connect the raspberry pi to a push button as shown below:

<img width="699" height="783" alt="ckt-diagram" src="https://github.com/user-attachments/assets/7319483f-635f-4d4b-88ba-5861e8c3bb0c" />

and run the automation script
```bash
python automate.py
```
and press the push button to run the entire scirpt.<br/>
still need the automate scirpt to start at boot

### stuff-left

- gps-stuff
- heat map of sand size distribution at the beach (also needs gps)
- web-app
- also a db for storing sand data
- scale calculation program
- automating the hardware, so the user can just use this like a camera
- adding the option to use images from your smartphone
- anything else??

still have a lot of parts to fulfill. i guess.

---

>"Grains of the golden sand, how few! yet how they creep, through my fingers to the deep."  -Edgar Allan Poe
