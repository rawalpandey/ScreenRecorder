import numpy as np
import cv2
import pyscreenshot as pys

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    #ret, frame = cap.read()
    img = pys.grab()
    img_np=np.array(img)
    out.write(img_np)
    cv2.imshow('frame',img_np)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()