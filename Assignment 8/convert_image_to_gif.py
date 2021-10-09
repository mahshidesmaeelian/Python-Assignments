import imageio
import os

my_files = os.listdir('photos')
images=[]

for i in range (len(my_files)):
    image=imageio.imread('photos/'+my_files[i])
    images.append(image)

imageio.mimsave('newgif.gif',images)   