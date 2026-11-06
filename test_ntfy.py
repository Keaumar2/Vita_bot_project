import requests


#le programme envoie une requête au serveur ntfy.sh , le serveur traite la requête et envoie une réponse.
#la réponse est stockée dans la variable response
response = requests.post('https://ntfy.sh/bot_vita_project', data='mon cul mon cul mon cul')

response_ntfy = requests.post('https://discord.com/api/webhooks/1566945223798431904/rwjhE40qZULUDpl4Z-VQG2TRIQI8u_l39qgHHFfL26Hkv5wZS2V8inPcUimqR0bCuVph', json={'content': 'mon cul mon cul mon cul'})

#il y a plusieurs informations stockées dans la variable response
#.text permet d'afficher l'information renvoyée par le serveur sous forme de texte c'est le corps de la réponse
print(response.text)