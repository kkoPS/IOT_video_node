### Module camera

#### Team Lederrey & Koubaa

Objectifs

REC **: Récupération et enregistrement caméra**

- Membres : YL et WK
- Objectifs
  - Le système sera capable de récupérer le flux vidéo d’une caméra (diurne et nocturne)
  - Le système sera capable d’enregistrer localement un flux vidéo

###1. Automatisation récupéreation du flux vidéo

- script pour enable la camera automatiquement

  enable sur les configs

  -> sudo raspi-config 

  -> interface option

  -> P1 camera
  
  
  cf. **enable_camera.sh**

Brouillon: raspistill -v -o test.jpg


###2. Automatisation enregistrement local du flux vidéo


Utilsiation de *motion*


picamera

sudo rpi-update

pour update le firmware du raspberry pi

- script pour connecter le raspberry pi au Reseau ? (wifi enterprise ou personnel)


###Useful commands and files

- sudo nano /etc/motion/motion.conf
- sudo service motion start
- sudo raspi-config
- sudo rpi-update (update le firmware pour utiliser la camera)



Semaine 2:

-apt upgrade et update
Puis 
installtion de vlc : apt install vlc

motion essai/raspivid essai