import numpy as np
from PIL import Image

def imresize(im, sz):
    """ Resize an image array using PIL """
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
    """ Histogram equalization of a grayscale image. """
    # Get image histogram
    imhist, bins  = np.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] #normalize

    # Use linear interpolation of cdf to find new pixel values
    im2 = np.interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf

def compute_avarage(imlist):
    """ Compute the average of a list of images."""
    # open first image and make into array of type float
    averageim = array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            ## Some code
            averageim += array(Image.open(imname))    
        except:
            print (imname + '...skipped')

    averageim /= len(imlist)

    # return average as uint8
    return array(averageim, 'uint8')
