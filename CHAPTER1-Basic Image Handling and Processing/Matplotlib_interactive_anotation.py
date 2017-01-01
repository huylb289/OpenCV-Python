import matplotlib.pyplot as plt
from PIL import Image
from pylab import * 

#Plotting Images, Points, and Lines
infile = '../Images/frog.png'
try:
    # read image to array
    im = array(Image.open('../Images/frog.jpg'))
    imshow(im)
    print ('Please click 3 points')
    x = plt.ginput(3)
    print ('You clicked', x)
    plt.show()
except IOError:
    print ("File ", infile, " cannot open")
    
