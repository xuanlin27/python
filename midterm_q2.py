import cv2
import numpy as np
import random

# Load input image
img = cv2.imread('baboon.png')

# Get the height and width of the input image
height, width, _ = img.shape

# Define the size of the ROI
roi_size = 100

# Define the number of ROIs to extract
num_rois = 10

# Initialize a counter for the ROI filenames
roi_counter = 1

# Iterate to extract ROIs
for i in range(num_rois):
    # Generate random coordinates for the top-left corner of the ROI
    x = random.randint(0, width - roi_size)
    y = random.randint(0, height - roi_size)
    
    # Extract the ROI from the input image
    roi = img[y:y+roi_size, x:x+roi_size]
    
    # Generate the filename for the ROI
    filename = f'ROI{roi_counter:02d}.bmp'
    
    # Save the ROI as a file
    cv2.imwrite(filename, roi)
    
    # Increment the ROI counter
    roi_counter += 1
