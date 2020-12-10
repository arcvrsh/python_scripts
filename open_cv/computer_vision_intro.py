import cv2
cam = cv2.VideoCapture(0) #webcam
while True:
    state,frame = cam.read()
    if state:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video',frame)
        cv2.imshow('gray filter',gray)
        key = cv2.waitKey(10)
        print(key)
        if key == 101: # to close camera press 'e' from keyboard
            break
    else:
        break
cam.release() # camera usage is stopped
cv2.destroyAllWindows()