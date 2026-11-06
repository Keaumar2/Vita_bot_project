from curl_cffi import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

#Envoie de la requête à HLTV
page_to_scrape1 = requests.get('https://www.hltv.org/team/9565/vitality#tab-matchesBox', impersonate="chrome")
print(page_to_scrape1.status_code)

#-------------------------------------
if page_to_scrape1.status_code != 200:
    print("HTTP error", page_to_scrape1.status_code)
    exit()
#-------------------------------------

#Stockage du fichier HTML de la page, plus précisément de la fenêtre de Vitality
html1 = page_to_scrape1.text
soup1 = BeautifulSoup(html1, "html.parser")

#Stockage du nombre de boutton de match trouvé sur la page de Vitality
boutons = soup1.find_all("a", class_="matchpage-button")
print(len(boutons))

#-------------------------------------
if len(boutons) == 0:
    print("No matches found")
    exit()
#-------------------------------------

#Stockage du lien du premier match trouvé sur la page de Vitality
lien = boutons[0].get("href")
print(lien)

#Envoie de la requête à HLTV pour chopper le fichier HTML du match
page_to_scrape2 = requests.get("https://www.hltv.org" + lien, impersonate="chrome") 
print(page_to_scrape2.status_code)

#-------------------------------------
if page_to_scrape2.status_code != 200:
    print("HTTP error", page_to_scrape2.status_code)
    exit()
#-------------------------------------

html2 = page_to_scrape2.text
soup2 = BeautifulSoup(html2, "html.parser")

#Stockage du nombre de temps trouvé sur la page de match 
temps = soup2.find_all("div", class_="time")
print(len(temps))

#-------------------------------------
if len(temps) == 0:
    print("No time elements found")
    exit()
#-------------------------------------

print(temps[0])

date = temps[0].get("data-unix")
print(date)

if date is None:
    print("No date found in the HTML")
    exit()

print(datetime.fromtimestamp(int(date)/1000))

now = time.time()
print(datetime.fromtimestamp(now))

delay = int( (int(date)/1000) - now )

if delay > 0 and delay < 1000000000000:
    response_ntfy = requests.post('https://ntfy.sh/bot_vita_project', data='sta ima brate')
    print(response_ntfy.text)

    response_discord = requests.post('https://discord.com/api/webhooks/1566945223798431904/rwjhE40qZULUDpl4Z-VQG2TRIQI8u_l39qgHHFfL26Hkv5wZS2V8inPcUimqR0bCuVph', json={'content': 'Vitality plays soon my little choubidoux !!!'})
else: 
    print("ima jos vremena za rakiju")