import cv2
import os
import datetime


# loding file
file = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Opening camera
camera = cv2.VideoCapture(0)


# Checking Camera access
# if not camera.isopened():
#     print("Camera as no access!!!!")

while True :
    # reading frame by camera
    r , frame=camera.read()

    #converting frame to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Detecting human face
    #(1.3 in this case) specifies how much the image size is reduced at each image scale
    # (4 in this case) specifies how many neighbors each candidate rectangle should have to retain it (how many face)
    human=file.detectMultiScale(gray,2.0,4)

    #Drawing rectangle around face
    # (0,0,255) color to rectangle ,  2 is how many face to detect
    for (x,y,a,b) in human:
        cv2.rectangle(frame,(x,y),(x+a,y+b),(0,0,255),2)
        #Displaying camera feed
        cv2.imshow("camera",frame)
# 
    # if cv2.waitKey(1) & 0xff == ord("r"):
    
        # Saving the current frame as an image
        img_save = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        cv2.imwrite(f"{img_save}.jpg", frame)

    if cv2.waitKey(1) & 0xff == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()


