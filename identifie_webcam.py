#!/usr/bin/env python
import cv2
import pickle
import numpy as np
import os

frontal = "C:\\Users\\teone\\Desktop\\3A-ESIEA\\COURS - S2\\_PST\\poppy_pyenv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"
profil = "C:\\Users\\teone\\Desktop\\3A-ESIEA\\COURS - S2\\_PST\\poppy_pyenv\\Lib\\site-packages\\cv2\\data\\haarcascade_profileface.xml"

if not os.path.exists(frontal):
    print("Le fichier video n'existe pas", frontal)
    quit()

if not os.path.exists(profil):
    print("Le fichier cascade n'existe pas", profil)
    quit()
#AJOUTER RECONNAISSANCE VISAGE GAUCHE ET DROIT ------------------------------------
face_cascade= cv2.CascadeClassifier(frontal)
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
id_image=0
color_info=(255, 255, 255)
color_ko=(0, 0, 255)
color_ok=(0, 255, 0)
face_min_size = 70

with open("labels.pickle", "rb") as f:
    og_labels=pickle.load(f)
    labels={v:k for k, v in og_labels.items()}

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    tickmark=cv2.getTickCount()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #AJOUTER RECONNAISSANCE VISAGE GAUCHE ET DROIT ------------------------------------
    faces=face_cascade.detectMultiScale(gray, scaleFactor=1.2,minNeighbors=4, minSize=(face_min_size, face_min_size))
    for (x, y, w, h) in faces:
        roi_gray=gray[y:y+h, x:x+w]
        #id_, conf=recognizer.predict(cv2.resize(roi_gray, (c.min_size, c.min_size)))
        id_, conf=recognizer.predict(roi_gray)
        if conf<=95:#Personne reconnu | indice de confiance (inverssement proportionnelle à la véracité de l'identité) ~80-100
             color=color_ok
             name=labels[id_].split("\\")[-1]
             #AJOUT DE LA RECONNAISSANCE VOCAL------------PUIS SYNTHESE VOCAL PARCE QUE LA PERSONNE EST RECONNU
        else:#Personne non reconnu
            color=color_ko
            name="Inconnu"
        label=name+" "+'{:5.2f}'.format(conf)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, color_info, 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color_info, 2)
    cv2.imshow('L42Project', frame)
    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break
    if key==ord('a'):
        for cpt in range(100):
            ret, frame=cap.read()

cv2.destroyAllWindows()
print("Fin")
