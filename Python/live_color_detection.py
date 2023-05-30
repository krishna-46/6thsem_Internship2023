import cv2
import numpy as np

lr = {'red': (0, 100, 100), 'green': (50, 100, 100), 'blue': (110, 100, 100), 'yellow': (30, 100, 100), 'orange': (5, 100, 100), 'pink': (150, 100, 100)}
ur = {'red': (10, 255, 255), 'green': (70, 255, 255), 'blue': (130, 255, 255), 'yellow': (50, 255, 255), 'orange': (25, 255, 255), 'pink': (170, 255, 255)}
color_names = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0), 'yellow': (0, 255, 255), 'orange': (0, 165, 255), 'pink': (203, 192, 255)}

cap = cv2.VideoCapture(0)

while True:
    r, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, (lower_range, upper_range) in zip(color_names.keys(), zip(lr.values(), ur.values())):
        mask = cv2.inRange(hsv, np.array(lower_range), np.array(upper_range))
        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color_names[color_name], 2)
                cv2.putText(frame, color_name, (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color_names[color_name], 2)
                
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()




