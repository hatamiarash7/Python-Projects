import cv2
camera_port = 1
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.VideoCapture(camera_port)
while(True):
    _,frame=img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(frame,(x+5,y-5),(x+w-5,y+h+5),(255,0,0),2)
        cv2.putText(frame,"Arash Hatami",(110,450),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,255,0,200,)
    cv2.imshow('img',frame)
    if cv2.waitKey(25) == 27:break
cv2.destroyAllWindows()
img.release()