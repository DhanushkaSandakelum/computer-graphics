import cv2 as cv

img = cv.imread("../assets/Photos/igi.png")
cv.imshow('IGI', img)

cv.waitKey(0)