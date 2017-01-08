from PIL import Image
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt

# Not complete yet

##Apply the label() function to a thresholded image of your choice. Use histograms
##and the resulting label image to plot the distribution of object sizes in the image.

def label(image = None,threshold = None):
    # get all index with pixel > than threshold
    idx = image[:,:] < threshold
    image[idx] *= 0
    return image
infile = '../Images/baboon.png'
im = np.array(Image.open(infile).convert('L'))
(nr,nc) = im.shape
(dx,dy) = np.gradient(np.double(im))
orientation = np.arctan(np.divide(dx,dy))
(x,y) = np.meshgrid(im.shape[0],im.shape[1])

orientationThreshold = label(orientation, 1)
u = dx
v = dy
plt.figure()
plt.imshow(orientationThreshold)
plt.title('Out')
##plt.quiver(x,y,u,v)
plt.show()


# Here
