import sys
from PIL import Image
from random import randint
from datetime import datetime
import imageio

def time():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

try:
    args = [int(sys.argv[i]) for i in (1,2,3,4)]

    assert sys.argv[5] == "0" or sys.argv[5] == "1"

    args.append(bool(int(sys.argv[5])))
    try:
        args.append(int(sys.argv[6]))
    except:
        args.append(2)

    assert args[0] == 1 or args[0] == 2
except:
    raise ValueError("/!\ Paramètres incorrects.")

if args[0] == 1:
    size = (args[1], args[3])
    gen = [randint(0, args[5]-1) for i in range(size[0])]
    im = Image.new(mode="RGB", size=size)

    with open("rule.txt", 'r') as f:
        rule = f.read()

    for i in range(size[0]):
        color = (255//(args[5]-1)) * (-gen[i]+(args[5]-1))
        im.putpixel((i,0),(color,color,color))

    for turn in range(1, size[1]):
        newLine = []
        for i in range(size[0]):
            pixel = eval(rule)
            newLine.append(pixel)
            color = (255//(args[5]-1)) * (-pixel+(args[5]-1))
            im.putpixel((i,turn),(color,color,color))
        gen = newLine
    
    im.save(f"images/{time()}.jpg", "JPEG")

else:
    size = (args[1], args[2])
    gen = [[randint(0, args[5]-1) for j in range(size[0])] for i in range(size[1])]
    im = Image.new(mode="RGB", size=size)

    with open("rule2.txt", 'r') as f:
        rule = f.read()
    
    for i in range(size[1]):
        for j in range(size[0]):
            color = (255//(args[5]-1)) * (-gen[i][j]+(args[5]-1))
            im.putpixel((j,i),(color,color,color))

    time = time()
    filenames = [f"images/{time}--0.jpg"]
    im.save(filenames[0], "JPEG")

    for turn in range(1, args[3]):
        newGen = []
        for i in range(size[1]):
            newLine = []
            for j in range(size[0]):
                pixel = eval(rule)
                newLine.append(pixel)
                color = (255//(args[5]-1)) * (-pixel+(args[5]-1))
                im.putpixel((j,i),(color,color,color))
            newGen.append(newLine)
        gen = newGen
        if args[4] or turn == args[3]-1:
            filenames.append(f"images/{time}--{str(turn)}.jpg")
            im.save(filenames[turn], "JPEG")
    if args[4]:
        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        imageio.mimsave(f'images/{time}.gif', images)
    print(f"Terminé ! Fin de l'execution : {time()}")