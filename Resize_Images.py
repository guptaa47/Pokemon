import os
from PIL import Image

os.chdir('Pokemon_images')
cwd = os.getcwd()
print(cwd)
for _,_,files in os.walk(cwd):
    for file in files:
        if file[-4:] == ".jpg":
            im = Image.open(file)
            im = im.resize((200,200))
            im.save("../Resized_Images/"+file[:-4]+".jpg")