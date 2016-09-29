import cv2
cam = cv2.VideoCapture(0)
s, img = cam.read()
winName = "Camera Capture"
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
while s:
    cv2.imshow( winName,img )
    s, img = cam.read()
    key = cv2.waitKey(10)
    if key == 27 :
        cv2.destroyWindow(winName)
        cam.release()
        break
print "Goodbye"
cv2.waitkey(0)