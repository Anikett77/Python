#Face Detection

import cv2
import cv2.data
import os

print(os.listdir(cv2.data.haarcascades))

classifier = cv2.CascadeClassifier(cv2.data.haarcascades + '/'
                                   + 'haarcascade_frontalface_alt.xml')
cam = cv2.VideoCapture(0)
while True:
    status,frame=cam.read()
    if not status:
        print("Camera is not Working")
        break
    faces = classifier.detectMultiScale(frame,1.3,5)
    print(faces)
    for face in faces:
        x1 = face[0]
        y1 = face[1]
        x2 = face[0]+face[2]
        y2 = face[1]+face[3]
        cv2.rectangle(frame,(x1,y1),(x2,y2),[255,0,0],2)
    cv2.imshow("Picture",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()