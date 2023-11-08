import cv2
import face_recognition
import os

known_face_encodings = []
known_face_names = []

known_faces_directory = ""

for filename in os.listdir(known_faces_directory):
    if filename.endswith(".jpg"):
        known_image = face_recognition.load_image_file(os.path.join(known_faces_directory, filename))
        known_face_encoding = face_recognition.face_encodings(known_image)[0]
        known_face_encodings.append(known_face_encoding)
        known_face_names.append(os.path.splitext(filename)[0])

image_to_recognize = face_recognition.load_image_file("")


face_locations = face_recognition.face_locations(image_to_recognize)
face_encodings = face_recognition.face_encodings(image_to_recognize, face_locations)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    name = 'unknown'

    for i, known_face_encoding in enumerate(known_face_encodings):
        result = face_recognition.compare_faces([known_face_encoding], face_encoding)
        if result[0]:
            name = known_face_names[i]
            break  

 
    cv2.rectangle(image_to_recognize, (left, top), (right, bottom), (100, 100, 255), 2)
    cv2.putText(image_to_recognize, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (10, 10, 255), 2)


cv2.imshow("Face Recognition", image_to_recognize)
cv2.waitKey(0)
cv2.destroyAllWindows()
