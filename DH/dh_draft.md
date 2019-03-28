# Deployement Helper

## démarrer au boot

### option .bashrc

petit script de test qui `logger` un message au login.

- script `test.sh`
  ```bash
  #! /bin/bash

  logger Hello-test-iot
  ```
- ajouter dans `~/.bashrc`
  ```bash
  [...]
  /home/camilo/HEIG_VD/iot/test.sh
  ```

- A chaque login le message est loggé dans `/var/log/syslog`

Problème : à chaque login, il faut un loggin et aussi à chaqte ouverture de terminal.

### option systemd

Pour executer après que des services soient activés (internet par exemple) il est recommandé d'utiliser systemd, que nous avons découvert dans [ce post][systemd].




[systemd]: https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files "Understanding Systemd Units and Unit Files"




### Hardware

- RPI 3B+
- RPI Camera Module
- RPI Shield Cellular IoT Application
- 

-----

## Sources

- [Create a custom Raspbian OS image for production. (Medium)[https://medium.com/platformer-blog/creating-a-custom-raspbian-os-image-for-production-3fcb43ff3630)
  - cloner image : on a les sources
  - on modifie les sources et ajouter les configurations
  - on constuit l'image
  - on la déploie


-----

## drafts

image rasbian : deploy.sh mettre scripts dans les sources rasbian et que tout se config tout seul.
adresses, menus, toussa toussa

clone et execute script


