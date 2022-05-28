import imageio

imageName = input("Images name : ")
maxName = int(input("Max name : "))

filenames = []

for i in range(maxName+1):
    filenames.append(f"{imageName}{i}.jpg")

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave(f'images/generated.gif', images)