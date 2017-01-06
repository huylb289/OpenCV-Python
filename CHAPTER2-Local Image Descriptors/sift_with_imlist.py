import sift
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import pydot
import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt
import os
import sift

# get images list
pathimages = './white_house/'
imagefiles = [f for f in listdir(pathimages) if isfile(join(pathimages, f))]
nbr_images = len(imagefiles)

# create feature list
featlist = [] 
for image in imagefiles:
    imname = pathimages + image
    siftname = image + '.sift'
    sift.process_image(imname, siftname)
    featlist.append(siftname)

matchscores = np.zeros((nbr_images, nbr_images))

for i in range(nbr_images):
    for j in range(i, nbr_images): # only compute upper triangle
        print (' comparing', imagefiles[i], imagefiles[j])

        l1,d1 = sift.read_features_from_file(featlist[i])
        l2,d2 = sift.read_features_from_file(featlist[j])

        matches = sift.match_twosided(d1, d2)

        nbr_matches = sum(matches > 0)
        print ('number of matches = ', nbr_matches)
        matchscores[i,j] = nbr_matches

# copy values
for i in range(nbr_images):
    for j in range(i+1,nbr_images): # no need to copy diagonal
        matchscores[j,i] = matchscores[i,j]


threshold = 2 # min number of matches needed to create link
g = pydot.Dot(graph_type='graph') # don't want the default directed graph
for i in range(nbr_images):
    for j in range(i+1,nbr_images):
        if matchscores[i,j] > threshold:
            # first image in pair
            im = Image.open(pathimages + imagefiles[i])
            im.thumbnail((100,100))
            filename = str(i)+'.png'
            im.save(filename) # need temporary files of the right size
            g.add_node(pydot.Node(str(i),fontcolor='transparent',
            shape='rectangle',image=filename))
            # second image in pair
            im = Image.open(pathimages + imagefiles[j])
            im.thumbnail((100,100))
            filename = './'+str(j)+'.png'
            im.save(filename) # need temporary files of the right size
            g.add_node(pydot.Node(str(j),fontcolor='transparent',\
                                  shape='rectangle',image=filename))
            g.add_edge(pydot.Edge(str(i),str(j)))
            
g.write_png('whitehouse.png')

##Warning: No such file or directory while opening 0.png
##Warning: No or improper image="0.png" for node "0"
##Warning: No such file or directory while opening 1.png
##Warning: No or improper image="1.png" for node "1"
##Warning: No such file or directory while opening 2.png
##Warning: No or improper image="2.png" for node "2"
##Warning: No such file or directory while opening 4.png
##Warning: No or improper image="4.png" for node "4"
##Warning: No such file or directory while opening 8.png
##Warning: No or improper image="8.png" for node "8"

##Warning: No such file or directory while opening 0.png
##Warning: No or improper image="0.png" for node "0"
##Warning: No such file or directory while opening 1.png
##Warning: No or improper image="1.png" for node "1"
##Warning: No such file or directory while opening ./2.png
##Warning: No or improper image="./2.png" for node "2"
##Warning: No such file or directory while opening 4.png
##Warning: No or improper image="4.png" for node "4"
##Warning: No such file or directory while opening ./8.png
##Warning: No or improper image="./8.png" for node "8"

