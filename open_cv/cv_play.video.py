import cv2
vid = cv2.VideoCapture('Video.mp4')
while True:
    state,frame = vid.read()
    if state:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video',frame)
        cv2.imshow('gray filter',gray)
        key = cv2.waitKey(1)
        print(key)
        if key == 101: # to close camera press 'e' from keyboard
            break
    else:
        break
vid.release() # camera usage is stopped
cv2.destroyAllWindows()