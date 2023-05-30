import cv2
import os
import datetime


# loding file
file = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Opening camera
camera = cv2.VideoCapture(0)

# Setting up video formatting
# formatting = cv2.VideoWriter_fourcc(*"XVID")

# Checking Camera access
# if not camera.isopened():
#     print("Camera as no access!!!!")

while True :
    # reading frame by camera
    r , frame=camera.read()

    #converting frame to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Detecting human face
    human=file.detectMultiScale(gray,1.3,4)

    #Drawing rectangle around face
    for (x,y,a,b) in human:
        cv2.rectangle(frame,(x,y),(x+a,y+b),(0,0,255),2)
        #Displaying camera feed
        cv2.imshow("camera",frame)

    if cv2.waitKey(1) & 0xff == ord("r"):
        # Saving the current frame as an image
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        cv2.imwrite(f"{current_time}.jpg", frame)


        # cv2.imwrite(f"{len(datetime.listdir()):%Y-%m-%d %H-%M-%S}.jpg",frame)
        # img_save = cv2.VideoWriter(f"vid{len(os.listdir()):03d}.jpg", formatting, 20.0, (640, 480))

    if cv2.waitKey(2) & 0xff == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()


