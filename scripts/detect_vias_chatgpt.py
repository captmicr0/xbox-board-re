import cv2
import numpy as np

# Read in the image
img = cv2.imread('board_1_6_top.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blurred, 50, 150)

# Dilate the edges to fill in small gaps
kernel = np.ones((3,3), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)

# Find contours in the image
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours and draw them on the image
for contour in contours:
    # Get the center and radius of the enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(contour)
    
    # Calculate the area of the contour
    area = cv2.contourArea(contour)
    
    # Calculate the expected area of the enclosing circle
    expected_area = np.pi * radius**2
    
    # Calculate the difference between the expected and actual area
    diff = abs(expected_area - area)
    
    # If the difference is small, the contour is likely circular
    if diff < expected_area * 0.2:
        cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)

# Display the image
cv2.imshow('Vias', img)

# Wait for the user to press a key
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
