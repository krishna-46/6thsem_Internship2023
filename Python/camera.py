import cv2
import os

# h=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # read the face data
h=cv2.CascadeClassifier('haarcascade_eye.xml') # read the face data
cam = cv2.VideoCapture(0) # accesss the camera
fou=cv2.VideoWriter_fourcc(*"XVID") # video formating code
rec=False
if not cam.isOpened():
    print("cam as no access")

while True:
    r,f =cam.read()
    g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY) # converting to gray form

    hum= h.detectMultiScale(g,1.3,5)# detecting human face

    #drow the rectangle around the face   
    for (x,y,a,b) in hum:
        cv2.rectangle(f,(x,y),(x+a,y+b),(255,0,128),10)

    cv2.imshow("camra",f) # display the window.
    # wait=cv2.waitKey(2)
    if cv2.waitKey(2) & 0xff==ord("r"):
        video=cv2.VideoWriter(f"vid{len(os.listdir()):03d}.mp4",fou,20.0,(640,480))
        print("started recording")
        rec=True

    if cv2.waitKey(2) & 0xff==ord("s"):
        video.release()
        print("stop recording")
        rec=False
    if rec:
        video.write(f)

    if cv2.waitKey(2) & 0xff==ord("p"):
        cv2.imwrite(f"photo{len(os.listdir()):04d}.jpg",f)
        print("photo capturedxx")
        i50-0 cv2.waitKey(2) & 0xff==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()


