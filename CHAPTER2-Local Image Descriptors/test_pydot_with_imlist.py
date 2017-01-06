import pydot

# get images list
path_images = './white_house/'
imagefiles = [f for f in listdir(pathimages) if isfile(join(pathimages, f))]
nbr_images = len(imagefiles)

threshold = 2 # min number of matches needed to create link
g = pydot.Dot(graph_type='graph') # don't want the default directed graph
for i in range(nbr_images):
    for j in range(i+1,nbr_images):
        if matchscores[i,j] > threshold:
            # first image in pair
            im = Image.open(imlist[i])
            im.thumbnail((100,100))
            filename = str(i)+'.png'
            im.save(filename) # need temporary files of the right size
            g.add_node(pydot.Node(str(i),fontcolor='transparent',
            shape='rectangle',image=path+filename))
            # second image in pair
            im = Image.open(imlist[j])
            im.thumbnail((100,100))
            filename = str(j)+'.png'
            im.save(filename) # need temporary files of the right size
            g.add_node(pydot.Node(str(j),fontcolor='transparent',\
                                  shape='rectangle',image=path+filename))
            g.add_edge(pydot.Edge(str(i),str(j)))
            
g.write_png('whitehouse.png')

