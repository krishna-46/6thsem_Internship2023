import cv2
import os


# haarcas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# haarcas = cv2.CascadeClassifier('haarcascade_eye.xml')
haarcas = cv2.CascadeClassifier('haarcascade_smile.xml')
cam= cv2.VideoCapture(0)
# fou=cv2.VideoWriter_fourcc(*"XVID")

while True:
    r,f=cam.read()
  
    g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)

    hum= haarcas.detectMultiScale(g,1.3,4)

    
    for (x,y,a,b) in hum:
        cv2.rectangle(f,(x,y),(x+a,y+b),(0,0,255),2)
    cv2.imshow("camra",f)

    if cv2.waitKey(2) & 0xff==ord("p"):
        cv2.imwrite(f"photo{len(os.listdir()):04d}.jpg",f)
        print("photo capturedxx")
    if cv2.waitKey(1) & 0xff==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()