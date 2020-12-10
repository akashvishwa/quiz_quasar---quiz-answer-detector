import numpy as np
import cv2

def clickImage():
    url = 'http://192.168.43.1:8080/video'
    cam = cv2.VideoCapture(url)

    cv2.namedWindow("Press Space-Click Image Esc-Quit")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Press Space-Click Image Esc-Quit", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            # img_name = "opencv_frame_{}.png".format(img_counter)
            img_name = "./resources/image.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

# clickImage()