# web_scraping
Faire un petit extracteur d'adresses e-mail de sites web (Data scraping)
zf200408.1258

## Buts

### En ce moment
C'est d'extraire les adresses e-mail de tous les EMS Vaudois

Il faut faire un petit scraper qui va *cliquer* sur chaque *image* pour aller récupérer l'adresse e-mail de l'EMS ;-)


### Source de données
On part de ce site qui a l'air d'avoir pas mal d'adresses d'EMS pour le canton de Vaud.

https://www.heviva.ch/institutions.html


## Moyens
### lib Python Beutifulsoup
On va le faire avec la lib Python Beutifulsoup


## Installation

### Pour MAC
brew install python3-pip
sudo /usr/bin/pip3 install --upgrade pip
sudo /usr/bin/pip3 install bs4
sudo /usr/bin/pip3 install requests

### Pour Linux
sudo apt-get install python3-pip
sudo pip install bs4
sudo pip install requests


### Utilisation
Pour récupérer la liste des descriptions des EMS sur https://www.heviva.ch/institutions.html:
```
./scrap_url_ems.py > url_list.txt
```

Pour récupérer la liste des adresses e-mail des EMS sur https://www.heviva.ch/institutions.html:


ATTENTION ne marche pas encore !


```
./scrap_email_ems.py > email_list.txt
```


### Sources

https://github.com/epfl-dojo/FMW

