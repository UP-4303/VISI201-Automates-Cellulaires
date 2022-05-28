import sys
from PIL import Image
from random import randint
from datetime import datetime
import imageio.v2 as imageio

def timeFunc():
    """
    Donne la date et l'heure actuelles, formatées pour être utilisées comme nom de fichier.
    """
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

try: # Récupération des valeurs passées dans la commande. Si un argument est invalide une erreur est levée
    args = [int(sys.argv[i]) for i in (1,2,3,4)]

    assert sys.argv[5] == "0" or sys.argv[5] == "1"
    assert sys.argv[6] == "0" or sys.argv[6] == "1"

    args.append(bool(int(sys.argv[5])))
    args.append(bool(int(sys.argv[6])))
    args.append(int(sys.argv[7]))

    assert args[0] == 1 or args[0] == 2
except:
    raise ValueError("/!\ Paramètres incorrects.")

if args[0] == 1: # Si l'automate est en 1D
    size = (args[1], args[3]) # Largeur, hauteur
    
    if args[5]: # Si on utilise une génération initiale aléatoire
        gen = [randint(0, args[6]-1) for i in range(size[0])]
    else:
        with open("start.txt", 'r') as f:
            gen = f.readlines()
        
        if len(gen) > 1 or len(gen[0]) > size[0]: # Si le contenu du fichier est trop grand, une erreur est levée
            raise ValueError("/!\ Génération de départ invalide.")
        else:
            right = True
            gen = list(gen[0]) # str -> list[str]
            gen = [int(i) for i in gen] # str -> int
            while len(gen) < size[0]: # On complète avec des 0
                if right:
                    gen.append(0)
                else:
                    gen.insert(0,0)
                right = not right # Alternance gauche/droite

    im = Image.new(mode="RGB", size=size) # Création de l'image avec le module PIL

    with open("rule.txt", 'r') as f: # Récupération de la règle
        rule = f.read()

    for i in range(size[0]): # On imprime la première génération en haut de l'image
        color = (255//(args[6]-1)) * (-gen[i]+(args[6]-1))
        im.putpixel((i,0),(color,color,color))

    for turn in range(1, size[1]):
        newLine = [] # Génération
        for i in range(size[0]):
            pixel = eval(rule) # On évalue la règle avec les valeurs actuelles pour chaque cellule
            newLine.append(pixel)
            color = (255//(args[6]-1)) * (-pixel+(args[6]-1))
            im.putpixel((i,turn),(color,color,color))
    
    im.save(f"images/{timeFunc()}.jpg", "JPEG") # On enregistre l'image

else: # Si l'automate est en 2D
    size = (args[1], args[2])

    if args[5]: # Si on utilise une génération initiale aléatoire
        gen = [[randint(0, args[6]-1) for j in range(size[0])] for i in range(size[1])]
    else:
        with open("start.txt", 'r') as f:
            gen = f.readlines()
        
        for i in range(len(gen)): # Conversion en list[list[int]]
            if i == len(gen)-1:
                gen[i] = list(gen[i])
            else:
                gen[i] = list(gen[i][:-1])
            if len(gen[i]) > size[0]: # Si la génération donnée est trop grande on lève une erreur
                raise ValueError("/!\ Génération de départ invalide.")
        if len(gen) > size[1]:
            raise ValueError("/!\ Génération de départ invalide.")

        down = True
        gen = [[int(j) for j in i] for i in gen]
        while len(gen) < size[1]: # On complète avec des lignes de 0
            if down:
                gen.append([0 for i in range(size[0])])
            else:
                gen.insert(0, [0 for i in range(size[0])])
            down = not down # Alternance haut/bas
        for i in range(len(gen)):
            right = True
            while len(gen[i]) < size[0]: # On complète la ligne avec des 0
                if right:
                    gen[i].append(0)
                else:
                    gen[i].insert(0,0)
                right = not right # Alternance gauche/droite


    im = Image.new(mode="RGB", size=size) # Création de l'image avec le module PIL

    with open("rule2.txt", 'r') as f: # Récupération de la règle
        rule = f.read()
    
    for i in range(size[1]): # Première image, correspondant à la génération initiale
        for j in range(size[0]):
            color = (255//(args[6]-1)) * (-gen[i][j]+(args[6]-1))
            im.putpixel((j,i),(color,color,color))

    time = timeFunc() # Heure de début
    filenames = [f"images/{time}--0.jpg"]
    im.save(filenames[0], "JPEG") # On enregistre la première image

    for turn in range(1, args[3]):
        newGen = []
        for i in range(size[1]):
            newLine = []
            for j in range(size[0]):
                pixel = eval(rule) # Evaluation de la règle avec les valeurs actuelles pour chaque cellule
                newLine.append(pixel)
                color = (255//(args[6]-1)) * (-pixel+(args[6]-1))
                im.putpixel((j,i),(color,color,color))
            newGen.append(newLine)
        gen = newGen
        if args[4] or turn == args[3]-1: # Si on enregistre chaque génération ou si c'est la dernière génération
            filenames.append(f"images/{time}--{str(turn)}.jpg")
            im.save(filenames[turn], "JPEG")
    if args[4]: # Si on enregistre chaque génération
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        imageio.mimsave(f'images/{time}.gif', images) # On fait un gif

print(f"Terminé ! Fin de l'exécution : {timeFunc()}") # On indique l'heure de fin à l'utilisateur, pour qu'il puisse connaître le temps d'exécution