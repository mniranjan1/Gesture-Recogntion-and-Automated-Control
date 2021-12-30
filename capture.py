import os
import time
import cv2
import imutils
import numpy as np

def init_create_folder():
    # create the folder and database if not exist
    if not os.path.exists("gestures"):
        os.mkdir("gestures")

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def store_images(g_name):

    camera = cv2.VideoCapture(0)
    total_pics = 40
    pic_no = 0
    flag_start_capturing = False
    frames = 0
    create_folder("gestures/"+str(g_name))
    while(True):
        (t, frame) = camera.read()

        frame = imutils.resize(frame, width=700)
        # flip the frame so that it is not the mirror view
        frame = cv2.flip(frame, 1)

        if frames > 150:
            cv2.imwrite("gestures/" + str(g_name)+"/"+ str(pic_no)+ str(g_name)+".jpg", frame)

            pic_no += 1
            st = int((pic_no)*100/total_pics)
            # draw the segmented hand
            cv2.putText(frame, "Capturing..." + str(st) + " %", (30, 60),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (127, 255, 255))

        cv2.imshow("Video Feed", frame)
        # observe the keypress by the user)

        # if the user pressed "Esc", then stop looping
        keypress = cv2.waitKey(1)
        if keypress == ord('q'):
            break
        if keypress == ord('c'):
            if flag_start_capturing == False:
                flag_start_capturing = True
            else:
                flag_start_capturing = False
                frames = 0
        if flag_start_capturing == True:
            frames += 1
        if pic_no == total_pics:
            break
    camera.release()
    cv2.destroyAllWindows()

init_create_folder()
g_name = input("Enter gesture name:")
store_images(g_name)