import cv2
img = cv2.imread('image' , cv2.IMREAD_GRAYSCALE)
ret,gpt = cv2.threshold(img , 80 , 210, cv2.THRESH_BINARY)
cv2.imshow('KOHARU' , gpt)
cv2.waitKey(0)
