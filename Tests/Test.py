import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
#out = cv2.VideoWriter('output.avi', fourcc, fps, (640, 480))

timepiece = 10
while(cap.isOpened()):
    namecount = 0
    out = cv2.VideoWriter('output' + str(namecount) +'.avi', fourcc, fps, (640, 480))
    namecount +=1
    count = 0
    while(count < (fps*timepiece)):
        ret, frame = cap.read()
        if ret==True:
           #frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)
            count+=1
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        out.release()
        break
    else:
        break

# Release everything if job is finished
cap.release()

cv2.destroyAllWindows()