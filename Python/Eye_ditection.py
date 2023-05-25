import cv2
import os

file = cv2.CascadeClassifier('haarcascade_eye.xml')

cam = cv2.VideoCapture(0)

vw=cv2.VideoWriter_fourcc(*"XVID")

if not cam .isOpened():
    print("cam as no access")

while True :
    r,frame = cam .read()

    gray_color = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    eye = file.detectMultiScale(gray_color,1.3,5)

    for (x,y,a,b) in eye :
        cv2.rectangle(frame(x,y),(x+a , y+b),(255,0,128),10)

    cv2.imshow("camra" , frame)

    if cv2.waitKey(2) & 0xff==ord("r"):
        video = cv2.VideoWriter(f"video{len(os.listdir()):03d}.mp4",vw,20.0,(640 , 480))
        print("  ssss")
        break
    cam.release()
    cv2.destroyAllWindows()