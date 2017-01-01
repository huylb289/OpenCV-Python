import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def get_imlist(path):
    """ Returns a list of filenames for
    all jpg and png images in a directory"""

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(('.jpg', '.png'))]

#Convert list images into gray scale
filelist = ['../Images/frog.jpg', '../Images/fruits.png']

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + "_grayscale" + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).convert('L').save(outfile)
        except IOError:
            print ("Cannot convert: ", infile)

