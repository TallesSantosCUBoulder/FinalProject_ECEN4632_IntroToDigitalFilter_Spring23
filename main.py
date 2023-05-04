# Program to indentify faces using python library

import face_recognition
from matplotlib import pyplot as plt
from matplotlib import image as mpimg



image = face_recognition.load_image_file("Picture_01.png")
face_locations = face_recognition.face_locations(image)


image = face_recognition.load_image_file("Picture_01.png")
face_landmarks_list = face_recognition.face_landmarks(image)


# print(face_landmarks_list)


plt.title("Teste")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")

plt.imshow(image)
plt.show()
