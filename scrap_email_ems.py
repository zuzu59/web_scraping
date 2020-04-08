#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Essai de récupération des adresses email sur la descrition des EMS sur https://www.heviva.ch/institutions.html

version = "0.1.2 zf200408.1544"

print("scrap_email_ems.py ver " + version)

import requests
from bs4 import BeautifulSoup

# EMS API - https://www.heviva.ch/institutions.html (en fait, il n'y en n'a pas :-(  )

url_site='https://www.heviva.ch'
html_page = requests.get(url_site+'/institutions.html')
#html_page = requests.get("https://api.fbi.gov/wanted/v1")
html_txt = html_page.text
soup = BeautifulSoup(html_txt, 'html.parser')
#names = soup.findAll("div", { "class" : "focuspoint" })
names = soup.findAll("a", { "class" : "item" })



def disp_debug():
    zurl_sites_EMS = scrap_email()
    for zitems in zurl_sites_EMS :
        ##print(zurl_sites_EMS[zitems])
        zhtml_page = requests.get(zurl_sites_EMS[zitems])
        zhtml_txt = zhtml_page.text
        zsoup = BeautifulSoup(zhtml_txt, 'html.parser')
        #print(zsoup)
        znames = zsoup.findAll("div", { "class" : "mail" })
        ##print(znames[0])
        # for zattribut in znames[0] :
        #     print(zattribut)
        #print(znames[0].attrs['href'])
        #print("toto")
        p1 = str(znames[0]).find('mailto:')
        p2 = str(znames[0]).find('"',p1)
        ##print(p1,p2)
        if p1 == -1 and p2 == -1 :
            #print("oups, y'a une erreur !.........................................")
            #print(str(znames[0]))
            p1 = str(znames[0]).find('http://')
            p2 = str(znames[0]).find('"',p1)
            #print(p1,p2)    
            zendcar = str(znames[0])[p2-1:p2]
            #print(zendcar)
            if zendcar == '.' or zendcar == ';' :
                #print("Y'a encore une erreur -------------------")
                p2 = p2 - 1
            if p1 == -1 and p2 == -1 :
                #print("oups, y'a une DEUXIEME erreur !.........................................")
                p1 = 0
                p2 = 0
            
        print(str(znames[0])[p1+7:p2])
        #print(str(znames[0]).find('mailto:'))
        #quit()
    
        
        
 

def scrap_email():
    zurl_sites_EMS = {}
    i = 0
    for zitems in names :
        zurl_site_EMS = url_site+'/'+zitems.attrs['href']
        zurl_sites_EMS[i] = zurl_site_EMS
        #print(zurl_sites_EMS[i]) 
        i = i +1
    return zurl_sites_EMS
    
    
    

if __name__ == '__main__':
#    print(getCriminals())
    disp_debug()
    
    
    