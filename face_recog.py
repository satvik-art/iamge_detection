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

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name='unknown'

        for i, known_face_encoding in enumerate(known_face_encodings):
            result = face_recognition.compare_faces([known_face_encoding], face_encoding)
            if result[0]:
                name = known_face_names[i]
                break  # Break the loop if a match is found
            
        cv2.rectangle(frame, (left, top), (right, bottom), (100, 100, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (10, 10, 255), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
