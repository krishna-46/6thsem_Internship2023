import cv2
import numpy as np

# Define color ranges for detection
color_ranges = {
    'red': [(0, 100, 100), (10, 255, 255)],
    'green': [(50, 100, 100), (70, 255, 255)],
    'blue': [(110, 100, 100), (130, 255, 255)],
    'yellow': [(30, 100, 100), (50, 255, 255)],
    'orange': [(5, 100, 100), (25, 255, 255)],
    'pink': [(150, 100, 100), (170, 255, 255)],
    'skin': [(0, 50, 50), (25, 255, 255)]
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        # result = cv2.bitwise_and(frame, frame, mask=mask)
        # result = cv2.rectangle(frame, frame, mask=mask)
        x,y,a,b = cv2.boundingRect(color)
        cv2.rectangle(frame,(x,y),(x+a , y+b),color[color_ranges],2)
        cv2.putText(frame , color , (x,y+20),cv2.FONT_HERSHEY_SIMPLEX , 0.75, color[color_ranges],2)

        cv2.imshow(f"{color.capitalize()} Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()