import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("../assets/Photos/paper.png")
cv.imshow("Source", img)
img_2 = img.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

template = cv.imread("../assets/Photos/paper_temp.png")
cv.imshow("Template", template)
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

h, w = template.shape

result = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

threshold = 0.7
location = np.where(result >= threshold)
for pt in zip(*location[::-1]):
    cv.rectangle(img_2, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)


cv.imshow("Match", img_2)

cv.waitKey(0)
cv.destroyAllWindows()