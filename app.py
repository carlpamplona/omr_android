import numpy as np
import cv2
import subprocess


cap = cv2.VideoCapture(2)


# create a function to handle mouse events
def capture(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # save the frame as an image
        cv2.imwrite('inputs/image.jpg', frame)
        print('Image captured!')
        subprocess.run(['python', 'main.py', '-a', '-i', './inputs'])


# create a window to display the frame
cv2.namedWindow('frame')

cv2.setMouseCallback('frame', capture)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    x1 = int(width * 0.4)
    y1 = int(height * 0.8)
    x2 = int(width * 0.6)
    y2 = int(height * 0.9)
    x3 = int(width * 0.4)
    y3 = int(height * 0.875)

    img = np.copy(frame)
    img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 10)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Capture', (x3, y3), font, 1, (255, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        print("Captured")
        break

cap.release()
cv2.destroyAllWindows()