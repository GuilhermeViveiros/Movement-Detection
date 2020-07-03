import time
import os
import numpy as np
from cv2 import *


def take_pictures():

    cap = cv2.VideoCapture(0)
    start = time.time()
    i = 0
    w = 0


    #ret, frame = cap.read()
    #frame = cv2.flip(frame,1)
    #cv2.imshow('frame',frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #break
    
    while i <= 1:

        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame',frame)
        #Este if serve para guardar as imagens em ordem crescente, 00,01..10,11,12...
        if w < 10:
            imwrite("Fotos/0" + str(w) + ".jpg", cv2.flip(frame, 1))
        else:
            imwrite("Fotos/" + str(w) + ".jpg", cv2.flip(frame, 1))

        w += 1

        ret, frame = cap.read()
        new_pic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        i = time.time() - start

    cap.release()
    cv2.destroyAllWindows()


take_pictures()