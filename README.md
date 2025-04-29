# Laser Speckle Analysis

For PHYS2210 Introduction to Experimental Physics (Spring 2025), I spent the semester analyzing intensity distributions of laser speckle. In this repo is all the code I used to analyze the data and produce the graphs, as well as the final poster.

```all_grit_analysis.py``` is the main program that analyzes the images and produces the graphs. It expects a specific file structure, detailed below. It saves all generated graphs in the ```outputs``` folder.

## Final Poster
![Final poster](final_poster/final_poster.png "Final poster as printed and presented")

## Expected File Structure
The ```all_grit_analysis.py``` program expects the following file structure. ```X_background.png``` is the background (black) image taken with the laser off. ```IMG_XXXX.png``` are the speckle images taken with the laser on for a given grit. 

```
📦phys_2210_photos
 ┣ 📂0_grit
 ┃ ┣ 📜0_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂1000_grit
 ┃ ┣ 📜1000_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂1500_grit
 ┃ ┣ 📜1500_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂150_grit
 ┃ ┣ 📜150_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂180_grit
 ┃ ┣ 📜180_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂240_grit
 ┃ ┣ 📜240_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂2500_grit
 ┃ ┣ 📜2500_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂3000_grit
 ┃ ┣ 📜3000_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂320_grit
 ┃ ┣ 📜320_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂400_grit
 ┃ ┣ 📜400_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂600_grit
 ┃ ┣ 📜600_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┣ 📂800_grit
 ┃ ┣ 📜800_background.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
 ┃ ┣ 📜IMG_XXXX.png
```

## Original Images
All images used for the analysis are availible to download [here](https://drive.google.com/drive/folders/1P8QvHCOnrvAMtI43O0iG7MU9QoY2lb_M?usp=sharing). They are not included in the 

## misc_programs
The ```misc_programs``` folder contains some other programs I wrote to help with the analysis, but they are not used in the main program. They are included for completeness and may be useful for reference. You must move them to the same directory as ```all_grit_analysis.py``` to run them.