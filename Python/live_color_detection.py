import cv2
import numpy as np


l_r= {"red":(166,84,141),'green':(25,52,72),'blue':(97,100,117),'yellow':(23,59,119)}
    #  ,'orange':(255, 191, 0),'pink':(255,0,255),'skin':(255,195,170)}

u_r={'red':(186,255,255),'green':(102,255,255),'blue':(117,255,255),'yellow':(54,255,255)}
    # ,'orange':(255,128,0),'pink':(255, 0, 128),'skin':(45,34,30)}

color_names={'red':(0,0,255),'green':(9,255,0),'blue':(255,0,0),'yellow':(0,255,217)}
#             #  ,'orange':(255,128,0),'pink':(255,0,128),'skin':(255,206,180)}

cap=cv2.VideoCapture(0)
while True:
# img = cv2.imread('test.jpg')

# Hue Saturation Value  
    r,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    for color_name , (l_r,u_r) in zip(color_names.keys(),zip(l_r.values(),u_r.values())):
        mask = cv2.inRange(hsv,np.array(l_r),np.array(u_r))
        kernel = np.ones((5,5),np.uint8)
        opening= cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

        c , hierarchy=cv2.findContours(opening,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in c :
            area = cv2.contourArea(cnt)
            if area > 1000:
                x,y,a,b = cv2.boundingRect(cnt)
                cv2.rectangle(frame,(x,y),(x+a , y+b),color_names[color_name],2)
                cv2.putText(frame , color_name , (x,y+20),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color_names[color_name],2)
                
    cv2.imshow("Image",frame)
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

# cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
            
            

# import cv2
# import numpy as np

# # Define the lower and upper boundaries for the HSV color space
# lower = np.array([0, 50, 50])
# upper = np.array([10, 255, 255])

# # Start the video capture
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture the frame
#     ret, frame = cap.read()
    
#     # Convert the frame from BGR to HSV color space
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     # Create a mask using the lower and upper boundaries
#     mask = cv2.inRange(hsv, lower, upper)
    
#     # Find the contours in the mask
#     contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Draw the contours on the frame
#     cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    
#     # Display the resulting frame
#     cv2.imshow('Color Detection', frame)
    
#     # Exit if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and destroy all windows
# cap.release()
# cv2.destroyAllWindows()
