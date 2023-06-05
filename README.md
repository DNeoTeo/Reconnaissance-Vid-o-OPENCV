### POPPY project - humanoïd robot

Dans le cadre du projet open-source POPPY Project, j'ai eu la chance de construire le robot et de développer toute la partie reconnaissance vidéo du POPPY.
Ce projet a pour but de s'initier à la robotique en partant d'un base avec un robot qui doit être entièrement assemblé après avoir imprimer tous les parties du corps en 3D

## Reconnaissance vidéo
Dans c'est programme en python, j'ai utilisé la librairie Open-CV pour pouvoir enregistrer les visages à apprendre et ensuite lancer la reconnaissance des visages appris.
La reconnaissance vidéo inclut 3 parties majeures de programmation en python. 

En premier lieu la partie d’enregistrement vidéo et création de la base de données contenant les photos qui vont permettre au POPPY de distinguer les personnes reconnues de celles qui ne le sont pas.

Puis nous avons la partie d’apprentissage qui va créer les fichiers dont un contient le schéma de reconnaissance de ce visage (à partir d’un algorithme) et un autre fichier qui associe chaque schéma de visage à un nom. On a différents points à améliorer pour avoir une reconnaissance vidéo optimale. On peut commencer par l’apport d’une database de photo très grande avec des photos de plusieurs angles différents tout en supprimant celles ayant une netteté insuffisante, qui risquerait d'engendrer des faux positifs.

Enfin on va écrire un programme qui va reconnaître s’il y a des visages (de profil ou de face) passant devant la caméra. Ces visages vont alors être comparés à notre fichier de schémas de visages. Si le visage est reconnu on va chercher son nom dans le second fichier d’apprentissage et on pourra autoriser les ordres prononcés.

## En cours de montage
# Les moteurs, vis, boulons...
![image](https://github.com/DNeoTeo/Reconnaissance-Video-OPENCV/assets/48857676/f8441d53-5657-451f-96cd-1460d1a9e58a)
# Les pièces en 3D...
![image](https://github.com/DNeoTeo/Reconnaissance-Video-OPENCV/assets/48857676/c2b67702-a4ff-49b8-9418-ab05d702fecb)
# En cours d'assemblage...
![image](https://github.com/DNeoTeo/Reconnaissance-Video-OPENCV/assets/48857676/bcd5788b-b6a2-43b4-b75a-28defd3516f3)
# Le montage fini !
![POPPY rasp](https://github.com/DNeoTeo/Reconnaissance-Video-OPENCV/assets/48857676/d7b017c3-3a2a-4e13-b75f-b8127aff5d9f)

## Les premier mouvement du POPPY 

Une vidéo [ici](https://github.com/DNeoTeo/Reconnaissance-Video-OPENCV/assets/48857676/4ab346a2-5f94-43b2-9d35-d3203d6b7c82) montre les premiers mouvement du robot. 

# Bibliographie
Voici tous les liens qui m'ont permis de réaliser ces programmes Reconnaissance vidéo:

https://www.datacorner.fr/reco-faciale-opencv-2/

https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml

http://tableauxmaths.fr/spip/spip.php?article209

https://www.youtube.com/channel/UCn09iU3hS5Fpxv0XniGv2FQ/videos

https://www.youtube.com/watch?v=-3xbAkCWJCc

https://www.youtube.com/watch?v=tsiy3DgAKHk

https://linuxtut.com/fr/c7791eff14db78393aff/

https://www.youtube.com/watch?v=WQeoO7MI0Bs

Pour plus de détail un rapport complet sous format PDF ([ici](METTRE LIEN))
