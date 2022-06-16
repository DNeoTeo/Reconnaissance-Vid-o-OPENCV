import cv2
import os
import numpy as np
import pickle

#Conseil pour améliorer l'apprentissage et la reconnaissance :
#Un dataset avec des photos d'angle de vue variés
#Supprimer les photos flous qui engendre des faux positifs 
#Avoir des photos de la même taille

image_dir='pic_classees'
current_id=0
label_ids={}
x_train=[]
y_labels=[]
face_min_size = 70

for root, dirs, files in os.walk(image_dir):
    if len(files):
        label=root.split("/")[-1]
        for file in files:
            if file.endswith("png"):
                path=os.path.join(root, file)
                if not label in label_ids:
                    label_ids[label]=current_id
                    current_id+=1
                id_=label_ids[label]
                image=cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), (face_min_size, face_min_size)) #Redmiensionnement
                #image=cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                fm=cv2.Laplacian(image, cv2.CV_64F).var() #Calcul de l'indice de neteté
                if(fm<250):#Ecarté les photos légèrement flous
                    print("Photo Exclu: ", path, fm)
                else:
                    x_train.append(image)#tableau d'image 
                    y_labels.append(id_)#tableau d'id
                                    #ces deux tableaux sont liés puisque la photo a son id correspondant
with open("labels.pickle", "wb") as f:#première argument nom du fichier
    pickle.dump(label_ids, f)#Association des id aux noms de la personne

x_train=np.array(x_train)
y_labels=np.array(y_labels)
recognizer=cv2.face.LBPHFaceRecognizer_create()#Fonction dédiée à la reconnaissance de visage
recognizer.train(x_train, y_labels)#tableaux ayant le même nombre d'élément
recognizer.save("trainner.yml")#Enregistrement des caractéristique des visages avec son id correspondant (nom du fichier en première argument)
