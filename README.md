# Visualiseur d'Automates Cellulaires par Mattéo LUQUE

Ce programme vous permet de visualiser l'automate cellulaire de votre choix. Pour cela, si vous souhaitez visualiser un automate en une dimension, donnez la règle de cet automate dans le fichier "rule.txt". Si il est en deux dimensions, donnez la règle dans "rule2.txt".

Une fois que cela est fait, vous pouvez lancer le script "main.py" depuis votre console avec les arguments dans l'ordre suivant :
* 0 => Nombre de dimensions. 1 ou 2
* 1 => Largeur d'une génération. Entier positif
* 2 => Hauteur d'une génération. Le paramètre est ignoré si l'automate n'a qu'une dimension. Entier positif
* 3 => Nombre de générations. Entier
* 4 => Conserver toutes les générations. 1 si vous souhaitez conserver une image toutes les générations, 0 sinon. Le paramètre est ignoré si l'automate n'a qu'une dimension. 0 ou 1
* 5 => Nombre d'états possibles. Par défaut 2. Entier positif

Pour l'écriture de vos règles :
* La génération précédente est la liste "gen".
* La cellule sur laquelle est appliquée la règle est en coordonnée [i] ou [i][j] si vous utilisez 2 dimensions.
* Notez que par simplicité technique l'espace utilisé n'est pas Z^d mais un tore dont vous définissez les dimensions dans les arguments. Pour un automate à une dimension, si vous utilisez la valeur d'une cellule avec une coordonnée superieur à i veuillez noter [(i+x)%size[0]]. Pour un automate à deux dimensions, si vous utilisez la valeur d'une cellule avec des coordonnées superieur à i ou j, veuillez noter [(i+x)%size[1]] et/ou [(j+y)%size[0]].

Quelques exemples de règles :
* Le jeu de la vie, 2D : (gen[i][j] and (gen[i-1][j-1]+gen[i-1][j]+gen[i-1][(j+1)%size[0]]+gen[i][j-1]+gen[i][(j+1)%size[0]]+gen[(i+1)%size[1]][j-1]+gen[(i+1)%size[1]][j]+gen[(i+1)%size[1]][(j+1)%size[0]] in [2,3])) or (not(gen[i][j]) and (gen[i-1][j-1]+gen[i-1][j]+gen[i-1][(j+1)%size[0]]+gen[i][j-1]+gen[i][(j+1)%size[0]]+gen[(i+1)%size[1]][j-1]+gen[(i+1)%size[1]][j]+gen[(i+1)%size[1]][(j+1)%size[0]] == 3))
* Règle élémentaire 110, 1D : (gen[(i+1)%size[0]] and (not(gen[i-1]) or not(gen[i]))) or (gen[i] and not(gen[(i+1)%size[0]]))
* Règle élémentaire 30, 1D : gen[i-1]^(gen[i]|gen[(i+1)%size[0]])
