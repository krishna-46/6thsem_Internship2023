# import cv2
# import os


# # haarcas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # haarcas = cv2.CascadeClassifier('haarcascade_eye.xml')
# haarcas = cv2.CascadeClassifier('haarcascade_smile.xml')
# cam= cv2.VideoCapture(0)
# # fou=cv2.VideoWriter_fourcc(*"XVID")

# while True:
#     r,f=cam.read()
  
#     g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)

#     hum= haarcas.detectMultiScale(g,1.3,4)

    
#     for (x,y,a,b) in hum:
#         cv2.rectangle(f,(x,y),(x+a,y+b),(0,0,255),2)
#     cv2.imshow("camra",f)

#     if cv2.waitKey(2) & 0xff==ord("p"):
#         cv2.imwrite(f"photo{len(os.listdir()):04d}.jpg",f)
#         print("photo capturedxx")
#     if cv2.waitKey(1) & 0xff==ord("q"):
#         break

# cam.release()
# cv2.destroyAllWindows()


# ------------------------------------------------------------------

# import cv2
# import os
# import datetime

# # Loading the face cascade classifier
# file = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# # Opening the camera
# camera = cv2.VideoCapture(0)

# while True:
#     # Reading frame from the camera
#     ret, frame = camera.read()

#     # Converting the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detecting human faces
#     humans = file.detectMultiScale(gray, 1.3, 4)

#     # Drawing rectangles around the detected faces
#     for (x, y, w, h) in humans:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

#     # Displaying the camera feed
#     cv2.imshow("Camera", frame)

#     if cv2.waitKey(1) == ord("r"):
#         # Saving the current frame as an image
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
#         cv2.imwrite(f"{current_time}.jpg", frame)

#     if cv2.waitKey(1) == ord("s"):
#         break

# # Releasing the camera and closing all windows
# camera.release()
# cv2.destroyAllWindows()



# --------------------------------------------------------------------------------------
# auto saving pic if it find the face




import cv2
import os
import datetime


# Loading the face cascade classifier
file = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Opening the camera
camera = cv2.VideoCapture(0)

while True:
    # Reading frame from the camera
    ret, frame = camera.read()

    # Converting the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting human faces
    humans = file.detectMultiScale(gray, 1.3, 4)

    # Drawing rectangles around the detected faces
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Saving the current frame as an image
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        cv2.imwrite(f"{current_time}.jpg", frame)

    # Displaying the camera feed
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord("s"):
        break

# Releasing the camera and closing all windows
camera.release()
cv2.destroyAllWindows()
