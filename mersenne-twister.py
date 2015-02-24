# -*- coding:utf-8 -*-

from client import *
from mersenne import *

# ----------------------------------------------------------------------------
# Fonctions utiles 
# -------------------------

def inverser(value):
    """
    Permet d'inverser le mersenne twister et de retourner le résultat.

    i.e: inverser(_f(x)) = x

    >>> mersenne = MersenneTwister()
    >>> x = 50
    >>> inverse = m._f(x)
    >>> inverse = inverser(inverse)
    >>> inverse
    50

    """
    # Inversion étape 4
    value ^= (value >> 18)

    # Inversion étape 3
    value ^= (value << 15) & 4022730752

    # Inversion étape 2 (?)
    value ^= (value << 7) & 5760
    value ^= (value << 7) & 802816
    value ^= (value << 7) & 220200960
    value ^= (value << 7) & 2415919104

    # Inversion étape 1 (plus de précision)
    value ^= (value >> 11) & 0xFFC00000
    value ^= (value >> 11) & 0x3FF800
    value ^= (value >> 11) & 0x7FF
    
    return value



"""
TP2 PAC - mersenne-twister
"""

URL = 'http://pac.bouillaguet.info/TP2/mersenne-twister/'


# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------

server = Server(URL)
response = server.query('challenge/monbailly')
chall = response['challenge']


# ----------------------------------------------------------------------------
# Synchronisation du mersenne avec le challenge
# -------------------------

m = MersenneTwister()
tmp = [inverser(chall[i]) for i in range(624)]
m.set_state(tmp)


# ----------------------------------------------------------------------------
# Calcul de la 1001e valeur
# -------------------------

# On cherche le dernière valeur du tableau
while(True):
    r = m.rand() 
    if r == chall[len(chall)-1]:
        break

# La suivante est la valeur recherchée
val = m.rand()


# ----------------------------------------------------------------------------
# Envoi de la réponse
# -------------------------

response = server.query('prediction/monbailly/' + str(val))
print(response) # status : OK


