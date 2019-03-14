# Projet IOT : Nœud raspberry pi d'enregistrement et streaming vidéo
__Printemps 2019__



Equipes (en italique les responsables) :


* **[REC](REC)**: Récupération et enregistrement caméra
  * Membres : _WK_ et YL
  * Objectifs
    * Le système sera capable de récupérer le flux vidéo d’une caméra (diurne et nocturne)
    * Le système sera capable d’enregistrer localement un flux vidéo
* **TVS** : Transmission d'un flux vidéo du Pi sur serveur cloud (streaming) (Transmission Video Stream)
  * Membres : _MJ_, OK et LS
  * Objectifs
    * Le système sera capable d’envoyer le flux vidéo en temps réel sur un serveur cloud (streaming) via Wi-fi
* **CTS** : Transmission d'information via le shield Raspberry Pi Cellular IoT Application (Communication Through Shield)
  * Membres : _LF_ et RS
  * Objectifs
    * Permettre la transmission d'information via le shield sur une plateforme comme celle de Swisscom
* **MS** : Script principal qui orchestre le tout (Main Script)
  * Membres : _JS_ et CJ
  * Objectifs
    * Doit proposer un moyen d'être contacté (API ?)  par le backend ou la plateforme Swisscom (à éclaircir) et doit pouvoir appeler un script si besoin de streamer
    * Doit stocker et permettre de gérer le stockage temporaire du flux video sur une fenêtre donnée, durant un temps t_before modifiable (par l'API ?) depuis l'extérieur. Doit être sauvegardé quand demandé par l'extérieur ainsi que durant un temps t_duration
* **DH** : Facilitation du déploiement (Deployment Helper)
  * Membres : _CPS_ et AN
  * Objectifs
    * Recherche d'un moyen pour faciliter le déploiement du software sur les raspberry pi (création d'un script (pour éviter de devoir tout refaire lorsqu'on ajoute une fonctionnalité) pour build une image Raspbian avec les softs produits déjà installés et configurés pour se lancer au démarrage afin de pouvoir juste burn l'image et démarrer le pi ?)



**Les produits de ces teams seront des scripts python 3 stockés sur le repository actuel, dans les dossiers des noms d'équipe en gras.**
