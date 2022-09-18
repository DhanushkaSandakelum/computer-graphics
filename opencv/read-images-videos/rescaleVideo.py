import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("Videos/cat.mp4")

while True:
    isTrue, frame = capture.read()

    rescaled_frame = rescaleFrame(frame, 0.8)

    cv.imshow('Video', rescaled_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.waitKey(0)