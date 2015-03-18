# -*- coding:utf-8 -*-

import os
import base64
import json

from client import *

# ----------------------------------------------------------------------------
# 
# -------------------------
NOM = "monbailly"
PREFIXE = "prefixe"
OUTPUT1 = "out1"
OUTPUT2 = "out2"
SUFFIXE = "PAC POWAAAAAAAAAAA"

os.system("echo -n " + NOM + " > " + PREFIXE)
os.system("dd if=/dev/urandom bs=" + str(512 - len(NOM)) + " count=1 >> prefixe")

os.system("./coll_finder.bin " + PREFIXE + " " + OUTPUT1 + " " + OUTPUT2)
os.system("echo -n " + SUFFIXE + " >> " + OUTPUT1)
os.system("echo -n " + SUFFIXE + " >> " + OUTPUT2)

# os.system("cat " + PREFIXE + " " + OUTPUT1 + " | md5sum")
# os.system("cat " + PREFIXE + " " + OUTPUT2 + " | md5sum")

URL = 'http://pac.bouillaguet.info/TP2/md5-collisions/'
server = Server(URL)

# os.system("cat " + OUTPUT1 + " | base64 > out64_1 ")
# os.system("cat " + OUTPUT2 + " | base64 > out64_2 ")

os.system("cat " + PREFIXE + " out64_1 | md5sum")
os.system("cat " + PREFIXE + " out64_2 | md5sum")

file = open("out64_1", 'r')
msg1 = file.read()
# print(msg1)

file = open("out64_2", 'r')
msg2 = file.read()
# print(msg2)

# file = open(OUTPUT1, 'r')
# msg1 = file.read()
# file = open(OUTPUT2, 'r')
# msg2 = file.read()
# file.close()

# print(msg1)
# print(msg2)

# dic = {0:str(base64.b16encode(msg1.encode())), 1:str(base64.b16encode(msg2.encode()))}
# print(dic)


# response = server.query('checker/monbailly', dic)
