import cv2, math
camera_port = 0
image_number = 0
ramp_frames = 30
frame = 0
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(camera_port)
def take_shot():
    retval, im = camera.read()
    return im
def snapshot():
    global image_number, frame
    for i in xrange(ramp_frames):
        temp = take_shot()
    print 'Taking image + ' , frame
    camera_capture = take_shot()
    file = "/home/hatamiarash7/OpenCV - Python/snapshot_temp/test_image" + str(image_number) + ".png" 
    image_number += 1
    frame += 15
    cv2.imwrite(file, camera_capture)
    return temp
while(True):
    global frame
    _,frame=camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(frame,(x+5,y-5),(x+w-5,y+h+5),(255,0,0),2)
        check = math.modf(frame , 60)
        if check == 0 : temp2 = snapshot()
    cv2.imshow('img',frame)
    if cv2.waitKey(25) == 27 : break
cv2.destroyAllWindows()
camera.release()