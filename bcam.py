import time
import cv2
from imutils import face_utils
import dlib
import sys
import logging as log
import datetime as dt
import time 

cascPath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)


video_capture = cv2.VideoCapture(0)
anterior = 0
image_count = 0
while True:
 

    # Capture image-by-image
    ret, image = video_capture.read()
    scale_percent = 80 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # Resize image
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        

    if anterior != len(faces):
        anterior = len(faces)
        save_face = image[y:y+h, x:x+w].copy()
        cv2.imwrite('dataset/test/{}.jpg'.format(image_count), save_face)
        log.info(str(len(faces))+" face detected at "+str(dt.datetime.now()))
        image_count += 1    
    cv2.imshow('Video', image)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', image)

    

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()