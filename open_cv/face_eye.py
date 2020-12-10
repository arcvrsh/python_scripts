import cv2
cam = cv2.VideoCapture(0)
face_finder = cv2.CascadeClassifier('models/face_cascade.xml')
eye_finder = cv2.CascadeClassifier('models/eye_cascade.xml')
while True:
    state,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_finder.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        eyes = eye_finder.detectMultiScale(gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 99:
        break
cam.release()
cv2.destroyAllWindows()