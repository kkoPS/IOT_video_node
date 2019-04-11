# Projet IOT : Nœud raspberry pi d'enregistrement et streaming vidéo
__Printemps 2019__

Equipes (en italique les responsables) :

* **REC** : Récupération et enregistrement caméra. Streaming sur un port local donné et stockage dans un buffer circulaire.

  * Membres : _WK_ et YL
  * Objectifs
    * Fournir les modifications apportées au pi initial pour pouvoir utiliser la caméra et les scripts existants
    * Le système sera capable de récupérer le flux vidéo d’une caméra (diurne et nocturne) et de le streamer via un buffer circulaire
    * Le système sera capable d’enregistrer localement un flux vidéo
* **TVS** : Transmission d'un flux vidéo chiffré du Pi sur le backend (streaming) (Transmission Video Stream)
  * Membres : _MJ_, OK et LS
  * Objectifs
    * Le système sera capable d’envoyer le flux vidéo local, après chiffrement, en temps réel sur un serveur cloud (streaming) via Wi-fi
    * Utiliser une librairie ou une méthode de chiffrement symétrique facilement implémentable en python et en NodeJS (backend)
* **CTS** : Transmission d'information via le shield Raspberry Pi Cellular IoT Application (Communication Through Shield)
  * Membres : _LF_ et RS
  * Objectifs
    * Permettre la transmission d'information via le shield sur une plateforme comme celle de Swisscom
* **MS** : Script principal qui orchestre le tout (Main Script)
  * Membres : _JS_ et CJ
  * Objectifs
    * Proposer une API pour pouvoir :
      * Être contacté par le backend pour le pairing. Pour cela, se référer au diagramme d'activité.
      * Editer ou consulter les temps t_before et t_after (ainsi que d'autres paramètres qui pourraient venir)
      * Recevoir l'instruction d'enregistrer la vidéo sur un fichier local (déclanchement local ou via l'API proposée) et le transmettre sur l'API du backend après enregistrement avec un petit texte précisant le déclancheur de la vidéo (_api-requested-<numéro de la demande>_ ou _movement-detected_ ou _button-trigered_, ...)
      * Fournir le streaming local suite à une demande via l'API proposée. Cela enclanche le streaming local, le chiffrement et l'envoi sur le port du backend convenu.
    * Pouvoir vérifier si son adresse publique a changé (suite à un redémarrage par exemple) et contacter le backend le cas échéant pour lui indiquer la nouvelle adresse. Doit s'authentifier (signe une partie du payload avec la clef **privée**).
* **DH** : Facilitation du déploiement (Deployment Helper)
  * Membres : _CPS_ et AN
  * Objectifs
    * Ecrire un script qui pull les sources pour lesquelles notre solution a été testée, qui les modifie selon les besoin des autres groupes (pour activer la caméra, le shield NFC, le shield pour la carte sim, lancer le script principal au démarrage...) et effectuer une configuration de base (fermer les ports,...). Cela permet la création d'une image qui peut ensuite être gravée sur une carte pour faciliter le déploiement (monter les composants sur le pi, mettre l'image et démarrer).
    * Ecrire un script qui vérifie si un fichier donné _/opt/nodeVideo/.authenticated_ existe. Si non, il faut [générer une paire de clef publique-privée](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) et écrire l'adresse IP publique et la clef **publique** sur le module NFC. Sinon, s'assurer que la mémoire NFC est bien vide (erase).
* **NFC** : Connexion avec le module NFC

  * Membres : _MJ_, OK et LS
  * Objectifs

    * Fournir les modifications apportées au pi initial pour pouvoir utiliser le shield NFC et les scripts existants
    * Proposer des méthodes pour read, write et erase sur la mémoire du module NFC

**Les produits de ces teams seront des scripts python 3 stockés sur le repository actuel, dans les dossiers des noms d'équipe en gras.**
