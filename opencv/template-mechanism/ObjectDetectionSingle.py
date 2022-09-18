import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("../assets/Photos/paper.png", 0) # Grayscale loading
template = cv.imread("../assets/Photos/paper_temp.png", 0) # Grayscale loading
h, w = template.shape

# Template matching methods
# Use all methods and accept what gives the best result
methods = [
    cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
    cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED
]

for method in methods:
    img2 = img.copy()
    result = cv.matchTemplate(img2, template, method) # convolution
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print(min_loc, max_loc)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv.rectangle(img2, location, bottom_right, (0, 0, 255), 2)
    cv.imshow("Match", img2)
    cv.waitKey(0)
    cv.destroyAllWindows()