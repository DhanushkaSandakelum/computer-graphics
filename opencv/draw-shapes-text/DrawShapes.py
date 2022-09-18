import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Balnk', blank)

# Paint a specific color
blank[:] = 0, 255, 0
cv.imshow('Green', blank)

# Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (250, 250), 50, (255, 0, 0), thickness=5)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (0, 0), (500, 500), (255, 0, 255), thickness=2)
cv.imshow('Line', blank)

# Show Text
cv.putText(blank, "Hello world", (100, 100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100, 100, 100), 2)
cv.imshow('Text', blank)

cv.waitKey(0)