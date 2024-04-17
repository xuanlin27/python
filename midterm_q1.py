import cv2
import numpy as np

# Set image size
size = 512

# Initialize the chessboard image
chessboard = np.zeros((size, size), dtype=np.uint8)

# Define the size of each square
square_size = size // 8

# Iterate over each square of the chessboard
for i in range(8):
    for j in range(8):
        # Define the starting point of the current square
        x_start = i * square_size
        y_start = j * square_size
        # Define the ending point of the current square
        x_end = x_start + square_size
        y_end = y_start + square_size
        # If the sum of the row and column indices is even, set the square to 255 (white), otherwise set it to 0 (black)
        if (i + j) % 2 == 0:
            chessboard[y_start:y_end, x_start:x_end] = 255

# Save the image to a file
cv2.imwrite('output.bmp', chessboard)
