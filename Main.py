import cv2
import time 
import os
import numpy as np
from query import queryclass 
import pyttsx3
import pickle
import face_recognition

def gritting(name=""):
    a = time.strftime('%H')
    b = int(a)
    if 9<=b<12:
        return pyttsx3.speak('good goodmorning {}'.format(name))
    elif 12<=b<16:
        return pyttsx3.speak('good afternoon {}'.format(name))
    elif 16<=b<19:
        return pyttsx3.speak('good evening {}'.format(name))
    else:
        return pyttsx3.speak('good night {}'.format(name))

def newFD():
    last_entry_times = {}
    emp_id_count = {}
    cap = cv2.VideoCapture(0)

    file = open('keku42/face_detection/newEncodeFile12.p', 'rb')
    encodewithID = pickle.load(file)
    file.close()
    encodelistknown, empID = encodewithID

    while True:
        ret, frame = cap.read()
        cv2.imshow('output', frame)

        if cv2.waitKey(1) & 0xFF == ord('h'):
            break

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cfaceframe = face_recognition.face_locations(img)
        encodecframe = face_recognition.face_encodings(img, cfaceframe)

        for encodeface, faceloc in zip(encodecframe, cfaceframe):
            matches = face_recognition.compare_faces(encodelistknown, encodeface)
            facedis = face_recognition.face_distance(encodelistknown, encodeface)

            if min(facedis) <= 0.4:
                matchIndex = np.argmin(facedis)
                print(empID[matchIndex])
                empID1 = empID[matchIndex].split('_')[0]
                print(empID1)
                name = empID[matchIndex].split('_')[1]
                print(name)
                emp_id = int(empID1)

                last_entry_time = last_entry_times.get(emp_id, 0)
                ctime = time.strftime('%H:%M:%S')
                tdate = time.strftime('%Y/%m/%d')
                current_time = time.time()

                if current_time - last_entry_time >= 180:
        
                    last_entry_times[emp_id] = current_time

                
                    emp_id_count[emp_id] = emp_id_count.get(emp_id, 0) + 1
                    print(emp_id_count)

                    if emp_id_count[emp_id] % 2 == 0:
                        a = queryclass()
                        Type = 'out'
                        b = a.insert_emp_attandace(emp_id, tdate, ctime, Type)
                        # c = gritting(name)
                        # print(c)
                        print(pyttsx3.speak('good bye {}'.format(name)))
                    else:
                        a = queryclass()
                        Type = 'in'
                        b = a.insert_emp_attandace(emp_id, tdate, ctime, Type)
                        c = gritting(name)
                        print(c)  
                        # print(pyttsx3.speak('good morning {} '.format(name)))
                    
                    # print("Last Entry Time: ", last_entry_time)
                    # print("Last Entry Times: ", last_entry_times)
                    # print("Emp ID Count: ", emp_id_count)

    cap.release()
    cv2.destroyAllWindows()
