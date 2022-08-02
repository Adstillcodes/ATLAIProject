#V1.01 of code for ATL project

import face_recognition
import cv2
import numpy as np
import csv
import os

from datetime import datetime
#opencv video capture settings
video_capture = cv2.VideoCapture(2)
#defining images
jobs_image = face_recognition.load_image_file("photos/SteveJobs.jpg")
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]

ratan_tata_image = face_recognition.load_image_file("photos/RatanTata.jpg")
ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]

ad_image = face_recognition.load_image_file("photos/ad_image.jpg")
ad_encoding = face_recognition.face_encodings(ad_image)[0]

known_face_encoding = [
jobs_encoding,
ratan_tata_encoding,
ad_encoding
]

known_face_names = [
    "Steve Jobs",
    "Ratan Tata",
    "Anvit Deshpande"
]

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s=True

#creating the attendance file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+' .csv', 'w+', newline = '')
lnwriter = csv.writer(f)

#opencv video capture 

while True: 
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0),fx=0.25,fy=0.25) #decreasing the size of the frame
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


            #entering names in the CSV file
            face_names.append(name)
            if name in known_face_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])

    #showing the output to the user
    cv2.imshow("attendance system", frame)
    #pressing "Q" to "quit"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
    
