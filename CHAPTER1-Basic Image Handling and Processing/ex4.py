from PIL import Image
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt

##Write a function that finds the outline of simple objects in images (for example, a
##square against white background) using image gradients.

infile = '../Images/baboon.png'
sigma = 3
im = np.array(Image.open(infile).convert('L'))
mask = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
im_out = filters.convolve(im, mask)

plt.figure()
plt.imshow(im_out)
plt.title('Out')
plt.show()


# Here
