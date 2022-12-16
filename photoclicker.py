
import time
import cv2
import sys
import logging as log
import datetime as dt
import time 

# cascPath = "haarcascade_frontalface_alt.xml"
# faceCascade = cv2.CascadeClassifier(cascPath)


video_capture = cv2.VideoCapture(0)
anterior = 0
image_count = 0
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        time.sleep(5)
        pass

    # Capture image-by-image
    ret, image = video_capture.read()
   
    if image_count <= 10: 
        cv2.imwrite('dataset/applex/{}.jpg'.format(image_count), image)
    if image_count >= 10:
        print("Done")
    
    
    image_count += 1    
    cv2.imshow('Video', image)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Display the resulting frame
    cv2.imshow('Video', image)

    

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

if image_count >= 10:
    sys.exit()
