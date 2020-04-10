#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Essai de récupération des adresses email sur la descrition des EMS sur https://www.heviva.ch/institutions.html

version = "0.1.5 zf200410.1713"
print("scrap_email_ems.py ver " + version)

import sys
import requests
from bs4 import BeautifulSoup

url_site='https://www.heviva.ch'
html_page = requests.get(url_site+'/institutions.html')
html_txt = html_page.text
soup = BeautifulSoup(html_txt, 'html.parser')
names = soup.findAll("a", { "class" : "item" })

def disp_debug():
    sys.stdout.write('"URL","Nom","email"\n')
    zurl_sites_EMS = scrap_email()
    for zitems in zurl_sites_EMS :
        zhtml_page = requests.get(zurl_sites_EMS[zitems])
        zhtml_txt = zhtml_page.text
        zsoup = BeautifulSoup(zhtml_txt, 'html.parser')        
        ztitre = zsoup.findAll("h1", { "class" : "header" })
        p1 = str(ztitre[0]).find('header">')
        p2 = str(ztitre[0]).find('<',p1)
        sys.stdout.write('"' + zurl_sites_EMS[zitems] + '","' + str(ztitre[0])[p1+8:p2] + '","')
        znames = zsoup.findAll("div", { "class" : "mail" })
        p1 = str(znames[0]).find('mailto:')
        p2 = str(znames[0]).find('"',p1)
        if p1 == -1 and p2 == -1 :
            p1 = str(znames[0]).find('http://')
            p2 = str(znames[0]).find('"',p1)
            zendcar = str(znames[0])[p2-1:p2]
            if zendcar == '.' or zendcar == ';' :
                p2 = p2 - 1
            if p1 == -1 and p2 == -1 :
                p1 = 0
                p2 = 0
        sys.stdout.write(str(znames[0])[p1+7:p2] + '"\n')
    
def scrap_email():
    zurl_sites_EMS = {}
    i = 0
    for zitems in names :
        zurl_site_EMS = url_site+'/'+zitems.attrs['href']
        zurl_sites_EMS[i] = zurl_site_EMS
        i = i +1
    return zurl_sites_EMS
    
if __name__ == '__main__':
    disp_debug()
    
