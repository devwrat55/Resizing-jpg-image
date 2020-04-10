import cv2
photo = cv2.imread("img11.jpg")

#original photo
"""
cv2.imshow('devwrat', photo)
cv2.waitKey()
cv2.destroyAllWindows()
"""

crop = photo[50:600, 200:750 ]
crop_resize = cv2.resize(crop, (150,150))
photo[0:150, 0:150] = crop_resize
cv2.imshow('devwrat', photo)
cv2.waitKey()
cv2.destroyAllWindows()