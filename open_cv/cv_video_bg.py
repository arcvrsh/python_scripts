import cv2
vid = cv2.VideoCapture('video.mp4')
bg = cv2.createBackgroundSubtractorMOG2()
while True:
    state, frame = vid.read()
    fgmask = bg.apply(frame)
    cv2.imshow('Original',frame)
    cv2.imshow('masked',fgmask)
    if cv2.waitKey(1) == 99:
        break
vid.release()
cv2.destroyAllWindows()