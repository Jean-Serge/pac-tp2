# -*- coding:utf-8 -*-

"""
TP2 PAC - padding-attack
"""


from client import *

SEED = str(5) 
URL = 'http://pac.bouillaguet.info/TP2/padding-attack/'
SERVER = Server(URL)


# ----------------------------------------------------------------------------
# Récupération du message chiffré
# -------------------------

# ciphertext + IV
response = SERVER.query('challenge/monbailly/' + SEED) 
print(response)











# ----------------------------------------------------------------------------
# Envoi de la réponse
# -------------------------

#response = SERVER.query('validation/monbailly/'+ SEED)
#print(response)
