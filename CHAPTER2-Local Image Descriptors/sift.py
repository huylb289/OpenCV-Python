import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt
import os

def process_image(imagename, resultname, params="--edge-thresh 10 --peak-thresh 5"):
    """ Process an image and save the results in a file """

    if imagename[-3:] != 'pgm':
        # create a pgm file
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'

    cmmd = "~/vlfeat/bin/glnxa64/sift {} --output={} {}".format(imagename, resultname, params)
    print (cmmd)
    os.system(cmmd)
    print ('processed', imagename, 'to', resultname)

def read_features_from_file(filename):
    """ Read feature properties and return in matrix form."""
##318.861 7.48227 25.5857 1.12001 1.68523 0 0 0 1 0 0 0 0 0 11 16 0 ...
##...
    f = np.loadtxt(filename)
    return f[:,:4],f[:,4:] # feature locations, descriptors

def write_features_to_file(filename, locs, desc):
    """ Save feature location and descriptor to file. """
    np.savetxt(filename, np.hstack((locs,desc)))

def plot_features(im,locs,circle=False):
    """ Show image with features. input: im (image as array),
    locs (row, col, scale, orientation of each feature). """
    
    def draw_circle(c,r):
        t = np.arange(0,1.01,.01)*2*np.pi
        x = r*np.cos(t) + c[0]
        y = r*np.sin(t) + c[1]
        plt.plot(x,y,'b',linewidth=2)
        
    plt.imshow(im)
    if circle:
        for p in locs:
            draw_circle(p[:2],p[2])
    else:
        plt.plot(locs[:,0],locs[:,1],'ob')
    plt.axis('off')
    
