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

#### unit

unit : abstraction/ressource que le système manage.

- sections [case_sentitive_name]
  - X- non standard sections
- key=value directives
- key= override
- 1, yes, on, true, 0, no, off, false, seconds

```bash
[Unit] # metadata
Description=
Documentation= # systemctl status
Requires= # list units must activated or FAIL, in //
Wants= #less strict, recommended for most dependencies, in //
BindsTo= # stop if other terminates
Before= # make list wait if activated in //
After= # list started before the current unit
Conflicts= # start -> termanate list
Condition...= # test prior starting unit, or skipped
Assert...=  # fail list -> fail current
```

...

### test setup

En suivant [ce blog][systemd-blink]. et avec un script de test

```bash
$ nano /home/pi/iot/dh_test.sh
```

```bash
#! /bin/bash

logger iot-wot-test

```

```bash
$ chmod +x dh_test.sh
$ ./dh_test.sh
$ tail /var/log/syslog 
Mar 28 16:05:19 raspberrypi pi: iot-wot-test
```

créer le service

```bash
$ sudo nano /lib/systemd/system/iot_dh.service
# dans nano
[Unit]
Description=Deploy Helper IoT-2019 Project
After=multi-user.target

[Service]
ExecStart=/usr/bin/bash /home/pi/iot/dh_test.sh

[Install]
WantedBy=multi-user.target

```

>  *multi-user.target* is the system state where control is given over to the user (a "multi-user shell") but before the X Windows System is started.

reconaitre le service par le systeme

```bash
$ sudo systemctl daemon-reload
```

> Note that you will need to enter this command every time you change your
> .service file, as systemd needs to know it has been updated.

dire que ca commence au boot

```bash
$ sudo systemctl enable iot_dh.service
Created symlink /etc/systemd/system/multi-user.target.wants/iot_dh.service → /lib/systemd/system/iot_dh.service.
```

reboot

```bash
$ sudo reboot
```

ca marche pas

```bash
$ systemctl status iot_dh.service 
● iot_dh.service - Deploy Helper IoT-2019 Project
   Loaded: loaded (/lib/systemd/system/iot_dh.service; enabled; vendor preset: enabled)
   Active: failed (Result: exit-code) since Thu 2019-03-28 16:10:27 UTC; 6min ago
 Main PID: 679 (code=exited, status=203/EXEC)

Mar 28 16:10:27 raspberrypi systemd[1]: Started Deploy Helper IoT-2019 Project.
Mar 28 16:10:27 raspberrypi systemd[1]: iot_dh.service: Main process exited, code=exited, status=203/EXEC
Mar 28 16:10:27 raspberrypi systemd[1]: iot_dh.service: Unit entered failed state.
Mar 28 16:10:27 raspberrypi systemd[1]: iot_dh.service: Failed with result 'exit-code'.

```



------------------

##### draft

The correct way to do this is to create a directory named after the unit file with `.d` appended on the end.  So for a unit called `example.service`, a subdirectory called `example.service.d` could be created.  Within this directory a file ending with `.conf` can be used to override or extend the attributes of the system's unit file.

.service, .mount, .target



FIXME : activer ssh par défaut !!






[systemd]: https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files "Understanding Systemd Units and Unit Files"

[systemd-blink]: https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-3-systemd "method 3: systemd"



----------------



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


