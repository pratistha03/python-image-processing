import numpy as np
import cv2
img = cv2.imread('image1.jpg')
# w,h = img.shape
def pixelVal(pxl,s1,s2, r1, r2):
    if(0<=pxl and pxl<=r1):
        return (s1/s2)*pxl
    elif(r1<pxl and pxl<=r2):
        return ((s2-s1)/(r2-r1))*pxl
    else:
        return ((255-s2)/255-r2)*(pxl-r2)+s2

r1=70
s1=0
r2=140
s2=255
pixelVal_vec = np.vectorize(pixelVal)
contrast_stretched=pixelVal_vec(img, s1,s2,r1,r2)
cv2.imwrite('contrast_stretch.jpg', contrast_stretched)
cv2.imshow('original ', img)
cv2.imshow("contrast_stretched", contrast_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()
