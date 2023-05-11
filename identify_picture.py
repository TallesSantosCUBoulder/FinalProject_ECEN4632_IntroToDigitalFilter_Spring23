## Reference: https://pypi.org/project/face-recognition/


## includes
import face_recognition
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg



# load pictures
picture_of_me = plt.imread("Diego_Image.jpeg")

plt.imshow(picture_of_me)
plt.show()
#picture_of_me = face_recognition.load_image_file("Picture_Michelle_Obama.png")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0] # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

# location
picture_of_me_location = face_recognition.face_locations(picture_of_me)


# examples
# unknown_picture = face_recognition.load_image_file("Picture_Michelle_Obama.png")
unknown_picture = face_recognition.load_image_file("FinalProjectFigure.jpg")
# unknown_picture = face_recognition.load_image_file("Picture_Barack_Obama_02.png")


# face recognition
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)

# face landmarks
face_landmarks_list = face_recognition.face_landmarks(picture_of_me)

# compare faces
n_people = np.size(unknown_face_encoding,0);
results = face_recognition.compare_faces(my_face_encoding, unknown_face_encoding)




## plot figures

# setting values to rows and column variables
# create figure
fig = plt.figure(figsize=(10, 7))

# setting values to rows and column variables
rows = 1
columns = 2

# reading images
Image1 = picture_of_me
Image2 = unknown_picture


# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)

# showing image
plt.imshow(Image1)
plt.axis('off')
plt.title("Reference")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(Image2)
plt.axis('off')
plt.title("Unknown photo")


# check if one of the faces is the reference
results = np.array(results)
x = np.where(results == True)

if np.size(x,1) == True:
    str_aux = ' Its a picture of me! Position %d' %(x[0][0])
else:
    str_aux = "It's not a picture of me!"
fig.suptitle(str_aux)

plt.show()



# plot the center of the face, when it is recognized
unknown_face_encoding[0]






# # # # # # ## plot the face landmarks
# # # # # #
# # # # # #
# # # # # # plt.rcParams["figure.figsize"] = [7.00, 3.50]
# # # # # # plt.rcParams["figure.autolayout"] = True
# # # # # # im = picture_of_me
# # # # # #
# # # # # # fig, ax = plt.subplots()
# # # # # # im = ax.imshow(im)
# # # # # #
# # # # # # #x = np.array(range(500))
# # # # # # #ax.plot(x, x, ls='dotted', linewidth=2, color='red')
# # # # # #
# # # # # # # x = np.array( face_landmarks_list[0]['bottom_lip'] )
# # # # # # # ax.plot(x[:,0], x[:,1], ls='dotted', linewidth=2, color='red')
# # # # # # #
# # # # # # # x = np.array( face_landmarks_list[0]['chin'] )
# # # # # # # ax.plot(x[:,0], x[:,1], ls='dotted', linewidth=2, color='black')
# # # # # # #
# # # # # # # x = np.array( face_landmarks_list[0]['left_eyebrow'] )
# # # # # # # ax.plot(x[:,0], x[:,1], ls='dotted', linewidth=2, color='pink')
# # # # # # #
# # # # # # # x = np.array( face_landmarks_list[0]['right_eyebrow'] )
# # # # # # # ax.plot(x[:,0], x[:,1], ls='dotted', linewidth=2, color='pink')
# # # # # # #
# # # # # # # x = np.array( face_landmarks_list[0]['nose_tip'] )
# # # # # # # ax.plot(x[:,0], x[:,1], ls='dotted', linewidth=2, color='yellow')
# # # # # # #
# # # # # # # x = np.array( face_landmarks_list[0]['right_eye'] )
# # # # # # # ax.plot(x[:,0], x[:,1], ls='dotted', linewidth=2, color='magenta')
# # # # # # #
# # # # # # # x = np.array( face_landmarks_list[0]['left_eye'] )
# # # # # # # ax.plot(x[:,0], x[:,1], ls='dotted', linewidth=2, color='magenta')
# # # # # #
# # # # # # x_center_face = np.array( picture_of_me_location )
# # # # # # ax.plot(x_center_face[0,1], x_center_face[0,0], marker='v', color="pink")
# # # # # # ax.plot(x_center_face[0,1], x_center_face[0,2], marker='v', color="pink")
# # # # # # ax.plot(x_center_face[0,3], x_center_face[0,0], marker='v', color="pink")
# # # # # # ax.plot(x_center_face[0,3], x_center_face[0,2], marker='v', color="pink")
# # # # # #
# # # # # # x_center_x = np.round( np.mean( [x_center_face[0,1] , x_center_face[0,3]] ))
# # # # # # x_center_y = np.round( np.mean( [x_center_face[0,0] , x_center_face[0,2]] ))
# # # # # # ax.plot(x_center_x, x_center_y, marker='v', color="red")
# # # # # #
# # # # # #
# # # # # # plt.show()



































