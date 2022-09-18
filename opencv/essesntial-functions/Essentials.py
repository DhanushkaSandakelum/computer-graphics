import cv2 as cv

img = cv.imread("../assets/Photos/anna.jpg")
cv.imshow("Anna", img)

# Converting to a grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge cascade - Canny edge detection
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny edges", canny)

# Dialating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding the image
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Cropping
cropped = img[50: 200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)