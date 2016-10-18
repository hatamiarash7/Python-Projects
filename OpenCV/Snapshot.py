import cv2
camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
def get_image():
    retval, im = camera.read()
    return im
for i in xrange(ramp_frames):
 temp = get_image()
print("Taking image...")
camera_capture = get_image()
file = "test_image.png" 
cv2.imwrite(file, camera_capture)
camera.release()
