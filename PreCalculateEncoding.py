## includes
import face_recognition
import numpy as np
import pickle

# load the reference picture
picture_of_me = face_recognition.load_image_file("Diego_Image.jpeg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0] # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
face_landmarks_list_picture_of_me = face_recognition.face_landmarks(picture_of_me)
datafile = open("encodedData.dat", 'ab')
datafile2 = open("landmarkData.dat", 'ab')
pickle.dump(my_face_encoding, datafile)
pickle.dump(face_landmarks_list_picture_of_me, datafile2)
datafile.close()