import cv2

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("cam as no access")

while True:
    r,f=cam.read()
    
    cv2.imshow("kj",f)
    # if cv2.waitKey(2) & 0xff==ord("s"):
    cv2.imwrite("abc.jpg",f)

    cam.release()
    cv2.destroyAllWindows()


