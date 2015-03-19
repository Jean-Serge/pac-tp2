#/bin/bash

NOM='monbailly'
SUFFIXE='PAC POWAAAAAAAAAAA'

# Création des fichiers prefixe et suffixe
echo -n $NOM > prefixe
echo -n $SUFFIXE > suffixe

# Le fichier suffixe est complété avec des bits aléatoires
dd if=/dev/urandom bs=`expr 512 - $(expr length $NOM)` count=1 >> prefixe 


# Génération des fichiers provocant une collision
./coll_finder/coll_finder prefixe out1 out2

# Concatener le prefixe avec les messages obtenus et le suffixe 
# pour obtenir les messages à transmettre
cat prefixe out1 suffixe > msg1
cat prefixe out2 suffixe > msg2

# Les 2 sommes doivent être les mêmes 
cat msg1.txt | md5sum
cat msg2.txt | md5sum

