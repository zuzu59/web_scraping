#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Essai de récupération des adresses email sur la descrition des EMS sur https://www.heviva.ch/institutions.html

version = "0.1.1 zf200408.1259"

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


#                 WIP




def disp_debug():
    #print(soup)
    #print(names[0].attrs['href'])

    for zitems in names :
        #print(zitems)
        print(url_site+'/'+zitems.attrs['href'])
     


    
    # criminals = {}
    # for criminal in names :
    #     url_personne = criminal.attrs['data-base-url'].split('@@')[0]
    #     name = criminal.img.attrs['alt']
    #     criminals[name] = url_personne
    # return criminals    
    


# def getCriminal_name(criminal):
#     return(name)
# 
# def getCriminal_detail(criminal):
#     url_personne = criminal.attrs['data-base-url'].split('@@')[0]
#     return(url_personne)
# 
# def getCriminals():
#     return(names)
# 
# def getCriminalsList():
#     criminals = {}
#     for criminal in names :
#         url_personne = criminal.attrs['data-base-url'].split('@@')[0]
#         name = criminal.img.attrs['alt']
#         criminals[name] = url_personne
#     return criminals    


    #print(url_personne.split('@@')[0])
#url_personne = names[0].attrs['data-base-url']
if __name__ == '__main__':
#    print(getCriminals())
    disp_debug()
    
    
    