import cv2

cam_port = 0
cam = cv2.VideoCapture(cam_port)

result, image = cam.read()

if result:
    cv2.imshow("Test", image)

    cv2.imwrite("Test.png", image)

    cv2.waitKey(0)
    cv2.destroyWindow("Test")
else:
    print("No image detected. Pleas try again!")

cam.release()