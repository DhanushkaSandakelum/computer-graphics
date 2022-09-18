import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Read source image
# Make a copy to show the matches
# Transform to grayscale to perform template matching
img = cv.imread("assets/eng_paper.png")
cv.imshow("Source", img)
img_2 = img.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Read  template image
# Transform to grayscale to perform template matching
template = cv.imread("assets/eng_paper_temp.png")
cv.imshow("Template", template)
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

# Determine the height, width of the template image
h, w = template.shape

# Match image and template using Template Matching Correlation Coefficient method
result = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

# Any match that equal or exceed the threshold value, considered as a valid match
# Then draw a red rectangle over that match
threshold = 0.8
location = np.where(result >= threshold)
for pt in zip(*location[::-1]):
    cv.rectangle(img_2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

# Show the final result
cv.imshow("Match", img_2)

cv.waitKey(0)
cv.destroyAllWindows()