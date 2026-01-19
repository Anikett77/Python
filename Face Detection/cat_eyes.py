import cv2
import cv2.data
import os

print(os.listdir(cv2.data.haarcascades))
file_name = 'haarcascade_frontalcatface_extended.xml'
file_name2 = 'haarcascade_eye.xml'
face_path = cv2.data.haarcascades + '/' + file_name
eye_path = cv2.data.haarcascades + '/' + file_name2
face_modal = cv2.CascadeClassifier(face_path)
eye_modal = cv2.CascadeClassifier(eye_path)
img = cv2.imread("pussy1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_modal.detectMultiScale(gray, 1.3, 5)
for face in faces:
    x1 = face[0]
    y1 = face[1]
    x2 = x1 + face[2]
    y2 = y1 + face[3]
    cv2.rectangle(img,(x1,y1),(x2,y2),[255,0,0], 2)
eyes = eye_modal.detectMultiScale(gray, 1.3, 5)
for eye in eyes:
    x1 = eye[0]
    y1 = eye[1]
    x2 = x1 + eye[2]
    y2 = y1 + eye[3]
    cv2.rectangle(img,(x1,y1),(x2,y2),[255,0,0], 2)
    
cv2.imshow("image", img)
cv2.waitKey(0)