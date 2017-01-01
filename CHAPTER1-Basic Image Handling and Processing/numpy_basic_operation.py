import numpy as np
import os
from PIL import Image
import imtools
from pylab import *

# Read image and cast to float
##im = np.array(Image.open('../Images/frog.jpg'))
##im_float = np.array(Image.open('../Images/frog.jpg').convert('L'), 'f')
##print (im.shape, im.dtype)
##print (im_float.shape, im_float.dtype)


# Get value from coordinates i,j, and color channel k
# value = im[i, j, k]

# Array slicing
##im[i, :] = im[j, :] #set values of row i with values from row j
##im[:, i] = 100 #set all values in column i to 100
##im[:100, :50].sum() #the sum of the values of the first 100 rows and 50 columns
##im[50:100, 50:100] #rows 50-100, columns 50-100 (100th not included)
##im[i].mean() #average of row i
##im[:, -1] #last column
##im[-2,:] #second to last row


def numpy_basic_operation():
    # Graylevel Transform
    try:
        infile = '../Images/frog.jpg'
        im = np.array(Image.open(infile).convert('L'))
        im2 = 255 - im #invert image
        im3 = (100.0/255) * im + 100 # clamp to interval 100...200
        im4 = 255.0 * (im/255.0)**2 # squared
        print(int(im.min()), int(im.max()))
        print(int(im2.min()), int(im2.max()))
        print(int(im3.min()), int(im3.max()))
        print(int(im4.min()), int(im4.max()))

        #Convert array back into image
        pil_im = Image.fromarray(im)
        pil_im2 = Image.fromarray(im2)
        
        #With im3 and im4 we need to convert them back into unit8
        pil_im3 = Image.fromarray(im3)
        pil_im4 = Image.fromarray(im4)

        # Create new figure for show histogram
        plt.figure()
        plt.imshow(im)
        
        # Create new figure for histogram
        plt.figure()
        hist(im.flatten(), 256)
        plt.title('Histogram im')
        plt.show()
        
    except IOError:
        print("Error open file ", infile)


if __name__ == "__main__":
    im = array(Image.open('../Images/frog.jpg').convert('L'))
    im2, cdf = imtools.histeq(im)
    plt.plot(cdf)
    plt.show()
    
