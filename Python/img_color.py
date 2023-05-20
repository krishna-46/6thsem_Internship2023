import cv2
import numpy as np

lr= {'red':(166,84,141),'green':(25,52,72),'blue':(97,100,117),'yellow':(23,59,119),'orange':(255, 191, 0),'pink':(255,0,255),'skin':(255,195,170)}

ur={'red':(186,255,255),'green':(102,255,255),'blue':(117,255,255),'yellow':(54,255,255),'orange':(255,128,0),'pink':(255, 0, 128),'skin':(45,34,30)}

color_names={'red':(0,0,255),'green':(102,255,255),'blue':(117,255,255),'yellow':(54,255,255),'orange':(255,128,0),'pink':(255,0,128),'skin':(255,206,180)}

img = cv2.imread('test.jpg')

# Hue Saturation Value  
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

for color_name , (lr,ur) in zip(color_names.keys(),zip(lr.values(),ur.values())):
    mask = cv2.inRange(hsv,np.array(lr),np.array(ur))
    kernel = np.ones((5,5),np.uint8)
    opening= cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    c , hierarchy=cv2.findContours(
        opening,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in c :
        area = cv2.contourArea(cnt)
        if area > 1000:
            x,y,a,b = cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+a , y+b),color_names[color_name],2)
            cv2.putText(img , color_name , (x,y+20),
                        cv2.FONT_HERSHEY_SIMPLEX , 0.75, color_names[color_name],2)
            
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
            
            


    