#!/usr/bin/env python
import cv2
import pickle
import numpy as np
import operator
import picamera
import picamera.array
import os
from time import sleep 

face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
id_image=0
color_info=(255, 255, 255)
color_ko=(0, 0, 255)
color_ok=(0, 255, 0)
marge=70
WIDTH=640
HEIGHT=480
face_min_size = 50

with open("labels.pickle", "rb") as f:
    og_labels=pickle.load(f)
    labels={v:k for k, v in og_labels.items()}

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution=(WIDTH, HEIGHT) 
        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            tickmark=cv2.getTickCount()
            gray=cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray, scaleFactor=1.2,minNeighbors=4, minSize=(face_min_size, face_min_size))
            for (x, y, w, h) in faces:
                roi_gray=gray[y:y+h, x:x+w]
                #id_, conf=recognizer.predict(cv2.resize(roi_gray, (c.min_size, c.min_size)))
                id_, conf=recognizer.predict(roi_gray)
                if conf<=95:#Personne reconnu | indice de confiance (inverssement proportionnelle à la véracité de l'identité) ~80-100
                    color=color_ok
                    name=labels[id_]
                else:#Personne non reconnu
                    color=color_ko
                    name="Inconnu"
                label=name+" "+'{:5.2f}'.format(conf)
                cv2.putText(stream.array, label, (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, color_info, 1, cv2.LINE_AA)
                cv2.rectangle(stream.array, (x, y), (x+w, y+h), color, 2)
            fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
            cv2.putText(stream.array, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color_info, 2)
            cv2.imshow('L42Project', stream.array)
            key=cv2.waitKey(1)&0xFF
            if key==ord('q'):
                break
            stream.seek(0)
            stream.truncate()   
cv2.destroyAllWindows()
print("Fin")
