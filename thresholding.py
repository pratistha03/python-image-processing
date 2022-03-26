import numpy as np
import cv2
img = cv2.imread('image1.jpg',0)
w,h=img.shape
th=100
thr_img=np.array(img)
thr_img=np.array(img)
# print(thr_img)
for x in range(w):
    for y in range(h):
        if thr_img[x,y]<=th:
            thr_img[x,y]=0
        else:
            thr_img[x,y]=255
cv2.imwrite('threshold_img.jpg', thr_img)
cv2.imshow('original ', img)
cv2.imshow("threshold", thr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
