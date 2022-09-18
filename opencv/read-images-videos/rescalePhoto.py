from turtle import width
import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Photos/1.png")
rescaled_img = rescaleFrame(img)
cv.imshow('IGI', rescaled_img)

cv.waitKey(0)