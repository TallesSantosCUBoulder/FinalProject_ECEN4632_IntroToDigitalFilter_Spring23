# Program to identify faces using python library and give coordinates (right or left)


## includes
import face_recognition
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pickle

# load the reference picture
picture_of_me = face_recognition.load_image_file("Diego_Image.jpeg")
datafile = open("encodedData.dat", 'rb')
datafile2 = open("landmarkData.dat", 'rb')
my_face_encoding = pickle.load(datafile)  # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
face_landmarks_list_picture_of_me = pickle.load(datafile2)
datafile.close()
datafile2.close()

# take the picture using the shell script
#os.system("./TakePicture.sh") Method 1
# Method 2
cam_port = 0
cam = cv2.VideoCapture(cam_port)
result, image = cam.read()
if result:
    cv2.imwrite("CurrentPicture.jpg", image)
else:
    print("No image detected. Pleas try again!")

cam.release()


# load the picture
unknown_picture = face_recognition.load_image_file("CurrentPicture.jpg")

# face recognition
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)

# face landmarks
face_landmarks_list_unknown_picture = face_recognition.face_landmarks(unknown_picture)
picture_of_me_location = face_recognition.face_locations(unknown_picture)

# compare faces
n_people = np.size(unknown_face_encoding,0);

mean_x = 0

if unknown_face_encoding:

    results = face_recognition.compare_faces(my_face_encoding, unknown_face_encoding)

    results = np.array(results)
    x = np.where(results == True)


    if np.size(x,1) == True:
        str_aux = ' Its a picture of me! Position %d' %(x[0][0])


        position_face_recognition = x[0][0]
        face_landmarks_list_unknown_picture[position_face_recognition]


        # plot the face landmarks


        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        im = unknown_picture

        fig, ax = plt.subplots()
        im = ax.imshow(im)

        x_center_face = np.array( picture_of_me_location )
        ax.plot(x_center_face[0,1], x_center_face[0,0], marker='v', color="pink")
        ax.plot(x_center_face[0,1], x_center_face[0,2], marker='v', color="pink")
        ax.plot(x_center_face[0,3], x_center_face[0,0], marker='v', color="pink")
        ax.plot(x_center_face[0,3], x_center_face[0,2], marker='v', color="pink")

        mean_x = (x_center_face[0,1]+x_center_face[0,3])/2
        mean_y = (x_center_face[0,0]+x_center_face[0,2])/2

        ax.plot(mean_x, mean_y, marker='v', color="black")

    else:
        str_aux = "It's not a picture of me!"


else:
    str_aux = "No faces were recognized!"


print("/n/n/n")
print(str_aux)
print(mean_x)
print("/n/n/n")


plt.show()
