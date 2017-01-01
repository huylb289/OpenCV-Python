import matplotlib.pyplot as plt
from PIL import Image
from pylab import *

#Plotting Images, Points, and Lines
infile = '../Images/frog.png'
try:
    # 1. Read image, draw, and show image
    # read image to array
    im = array(Image.open('../Images/frog.jpg'))

    # create new figure
    plt.figure()

    # plot the image
    plt.imshow(im)

    # some points
    x = [100, 100, 400, 400]
    y = [200, 500, 200, 500]

    # plot the points with red star-markers
##    plt.plot(x, y, 'r*')
    plt.plot(x, y, 'go-')
##    plt.plot(x, y, 'ks:') 

    # line plot connecting the first two points
    plt.plot(x[:2], y[:2], 's:') # [100,100] and [200, 500]s

    # add title and show the plot
    title('Plotting: "frog.jpg"')

    # 2. Read image and show contour, histogram
    # read image to array
    im_gray = array(Image.open('../Images/frog.jpg').convert('L'))

    # create new figure
    plt.figure()

    # don't use colors
    plt.gray()
    # show contour with origin upper left corner
    plt.contour(im_gray, origin='image')
    plt.axis('equal')
    plt.title('Contour')
    
    plt.figure()
    hist(im_gray.flatten(), 128)
    plt.title('Histogram')

##    plt.axis('off') # turn off axis
    plt.show()    
except IOError:
    print ("File ", infile, " cannot open")

