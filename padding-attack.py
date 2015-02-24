# -*- coding:utf-8 -*-

"""
TP2 PAC - padding-attack
"""

from helpers import *
from client import *
import base64
import json

SEED = str(1) 
URL = 'http://pac.bouillaguet.info/TP2/padding-attack/'
SERVER = Server(URL)


# ----------------------------------------------------------------------------
# Récupération du message chiffré
# -------------------------

# ciphertext + IV (Initialization Vector)
response = SERVER.query('challenge/monbailly/' + SEED) 
print(response)


mess = Message(response['ciphertext']) # block.encode() - ligne 42
# length = mess.__len__()
# print(mess.__getitem__(length -1))

dic = {'ciphertext':str(mess)}
dic = json.dumps(dic)
print(dic)


response = SERVER.query('oracle/monbailly', dic)
print(response)







# ----------------------------------------------------------------------------
# Envoi de la réponse
# -------------------------

#response = SERVER.query('validation/monbailly/'+ SEED)
#print(response)
