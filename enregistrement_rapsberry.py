import cv2
import operator
import picamera
import picamera.array
import os
from time import sleep 

img_non_classees='pic-non-classees'
pic_name = "eduardo"
id=0
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
marge=70
WIDTH=640
HEIGHT=480
face_min_size = 70

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution=(WIDTH, HEIGHT)            
        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            tab_face=[] #tableau de visage
            tickmark=cv2.getTickCount()
            #Reconnaissance visage de face
            gray=cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)#convertion de l'image capturée en noir et blanc, on peut faire d'autre traitement avec cette methode
            face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(face_min_size, face_min_size))#Tous les rectangles en dessous de cette taille sont éliminés
            for x, y, w, h in face:
                tab_face.append([x, y, x+w, y+h])
            #Reconnaissance profil gauche
            face=profile_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(face_min_size, face_min_size))
            for x, y, w, h in face:
                tab_face.append([x, y, x+w, y+h])
            gray2=cv2.flip(gray, 1)#symétrie verticale 0 horizontale 1
            #Reconnaissance profil droit
            face=profile_cascade.detectMultiScale(gray2, scaleFactor=1.2, minNeighbors=4, minSize=(face_min_size, face_min_size))
            for x, y, w, h in face:
                tab_face.append([WIDTH-x, y, WIDTH-(x+w), y+h])#WIDTH-x car on inverse l'image
            tab_face=sorted(tab_face, key=operator.itemgetter(0, 1))
            #Affichage des rectangles autour des visages
            index=0
            
            for x, y, x2, y2 in tab_face:#position en haut à gauche et la taille du rectangle
                if not index or (x-tab_face[index-1][0]>marge or (y-tab_face[index-1][1])>marge):
                    cv2.imwrite("{}/{}_{:d}.png".format(img_non_classees, pic_name, id), stream.array[y:x2, x:y2])
                    cv2.rectangle(stream.array, (x, y), (x2, y2), (0, 0, 255), 2)#dessiner un rectangle sur l'image | position initiale | position d'arrivé | couleur | epaisseur de trait
                    id+=1
                    #sleep(1.5)
                index+=1
            if cv2.waitKey(1)&0xFF==ord('q'):#appuie sur lettre q et sorti du programme
                break
            
            #Affichage des FPS
            fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)#Calcul du framerate
            cv2.putText(stream.array, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)#image | le texte à afficher | position | font | epaisseur du trait | couleur | type de trait
            cv2.imshow('video', stream.array)
            stream.seek(0)
            stream.truncate()  
            for cpt in range(4):
                camera.capture(stream, 'bgr', use_video_port=True)
cv2.destroyAllWindows()
