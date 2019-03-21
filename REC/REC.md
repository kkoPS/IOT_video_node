### Module camera

#### Team Lederrey & Koubaa

Objectifs

REC **: Récupération et enregistrement caméra**

- Membres : YL et WK
- Objectifs
  - Le système sera capable de récupérer le flux vidéo d’une caméra (diurne et nocturne)
  - Le système sera capable d’enregistrer localement un flux vidéo

1.Automatisation récupéreation du flux vidéo

- script pour enable la camera automatiquement

  enable sur les configs

  -> sudo raspi-config 

  -> interface option

  -> P1 camera
  
  
  cf. **enable_camera.sh**

Brouillon: raspistill -v -o test.jpg


2.Automatisation enregistrement local du flux vidéo


Utilsiation de *motion*


picamera

rpi-update pour update le firmware du raspberry pi

- script pour connecter le raspberry pi au Reseau ? (wifi enterprise ou personnel)
