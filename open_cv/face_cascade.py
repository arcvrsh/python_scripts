import cv2 as cv
cam = cv.VideoCapture(0)
face_finder = cv.CascadeClassifier('models/face_cascade.xml')
while True:
    state,frame = cam.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face_finder.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,
                     pt1 = (x,y),
                     pt2 = (x+w,y+h),
                     color = (0,255,255),
                     thickness = 2
                    )  
    cv.imshow('frame',frame)
    k = cv.waitKey(1)
    if k == 99:
        break
cam.release()
cv.destroyAllWindows()