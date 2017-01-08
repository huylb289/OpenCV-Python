import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt
import os


def process_image(imagename, resultname, params="-t 50 -n 9"):
    """ Process an image and save the results in a file """
##Usage:
##
##fast [ -hlnsbt ] [input_image [output_file]]
##
##Options:
##
##input_image        Input filename (default is stdin)
##output_file        Output filename (default is stdout)
##-l                 Output a list of corners (instead of an image)
##-t X               Set threshold to X. Default is 20
##-n X               Use X point fast (allowed range is 9--12, default is 9)
##-s                 Perform nonmaximal suppression
##-b                 Display bibtex entries
##-h                 Display help message
##example:
##
##fast picture.jpg detected_corners.jpg
    
    if imagename[-3:] != 'pgm':
        # create a pgm file
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'

    cmmd = "~/fast/fast-Linux-x86_64 {} {} {} ".format(params, imagename, \
                                                             resultname)
    print (cmmd)
    os.system(cmmd)
    print ('processed', imagename, 'to', resultname)
