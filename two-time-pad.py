# -*- coding:utf-8 -*-

from client import *
import base64

# ----------------------------------------------------------------------------
# Fonctions utiles 
# -------------------------

def xor(a, b):
    """
    Effectue le xor de 2 chaines de
    bytes.
    """
    c = bytearray()
    for x,y in zip(a,b):
        c.append(x ^ y)
    return c

"""
TP2 PAC - two-time-pad
"""

URL = 'http://pac.bouillaguet.info/TP2/two-time-pad/'
SEED = str(5)


# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------
server = Server(URL)
response = server.query('challenge/monbailly/' + SEED)

# Récupération des champs (hexa)
AxorM = response['A']
BxorM = response['B']

# Décodage des champs (hexa->bytes())
AxorM = base64.b16decode(AxorM, casefold = True)
BxorM = base64.b16decode(BxorM, casefold = True)

# Retrait du masque
AxorB = xor(AxorM, BxorM)


# ----------------------------------------------------------------------------
# Récupération du message
# -------------------------
length = len(AxorB)
msg = ""
cpt = 0

# On parcours les octets i de la chaîne
for i in (AxorB):
    c = chr(i ^ ord('0'))
    
    # Si i xor '0' n'est pas un caractère, on garde i xor '1'
    if not(c.isalpha() or c == '\n' or c == ' '):
        c = chr(i ^ ord('1'))
    msg += str(c)


# ----------------------------------------------------------------------------
# Récupération de la question
# -------------------------
response = server.query('question/monbailly/' + SEED)

n_ligne = response['line']
n_mot = response['word']
print(n_ligne)
print(n_mot)
print(msg)
mot_cherche = ""

# ----------------------------------------------------------------------------
# Recherche du mot demandé
# -------------------------
nb_mot = 0
nb_ligne = 0

for i in msg:
    # On compte les lignes
    if i == '\n':
        nb_ligne += 1
        nb_mot = 0
    # On compte les mots
    if i == ' ':
        nb_mot += 1
    # On a trouvé le mot (on ignore les séparateurs)
    if nb_ligne == n_ligne and nb_mot == n_mot and i != ' ' and i != '\n':
        mot_cherche += i


# ----------------------------------------------------------------------------
# Envoi de la réponse
# -------------------------
dic = {'word' : mot_cherche}

response = server.query('answer/monbailly/' + SEED, dic)
print(response) # {'status' : 'OK'}
