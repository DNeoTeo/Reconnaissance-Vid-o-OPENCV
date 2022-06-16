from time import sleep
import cv2
import operator
import os

from nbformat import current_nbformat_minor

img_non_classees='pic-non-classees'
pic_name = "XVI"
for root, dirs, files in os.walk(img_non_classees):
    id=0
    if(len(files)):
        current_id=0
        for file in files:
            current_id=int(file.split("_")[-1].split(".")[0])
            if(current_id>id):
                id=current_id
print(id)
frontal = "C:\\Users\\teone\\Desktop\\3A-ESIEA\\COURS - S2\\_PST\\poppy_pyenv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml"
profil = "C:\\Users\\teone\\Desktop\\3A-ESIEA\\COURS - S2\\_PST\\poppy_pyenv\\Lib\\site-packages\\cv2\\data\\haarcascade_profileface.xml"

if not os.path.exists(frontal):
    print("Le fichier video n'existe pas", frontal)
    quit()

if not os.path.exists(profil):
    print("Le fichier cascade n'existe pas", profil)
    quit()

if not os.path.isdir(img_non_classees):
    os.mkdir(img_non_classees)

face_cascade=cv2.CascadeClassifier(frontal)
profile_cascade=cv2.CascadeClassifier(profil)
cap=cv2.VideoCapture(0)
width=int(cap.get(3))#.get 3 largeur 4 hauteur
marge=80
face_min_size = 70

while True:
    ret, frame=cap.read()
    tab_face=[] #tableau de visage
    tickmark=cv2.getTickCount()
    #Reconnaissance visage de face
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#convertion de l'image capturée en noir et blanc, on peut faire d'autre traitement avec cette methode
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(face_min_size, face_min_size))#Tous les rectangles en dessous de cette taille sont éliminés
    for x, y, w, h in face:
        tab_face.append([x, y, x+w, y+h])
    #Reconnaissance profil gauche
    face=profile_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(face_min_size, face_min_size))
    for x, y, w, h in face:
        tab_face.append([x, y, x+w, y+h])
    #Reconnaissance profil droit (problème lors de l'écriture du fichier)
    #fin test
    #Affichage des rectangles autour des visages
    index=0
    for x, y, x2, y2 in tab_face:
        if not index or ((x-tab_face[index-1][0])>marge or (y-tab_face[index-1][1])>marge):
            cv2.imwrite("{}/{}_{:d}.png".format(img_non_classees, pic_name, id), frame[y:y2, x:x2])
            sleep(0.2)
            cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
            id+=1
            
        index+=1
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('video', frame)
    for cpt in range(4):
        ret, frame=cap.read()
    
cap.release()
cv2.destroyAllWindows()
