from PIL import Image
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt

##Implement an unsharp masking operation (http://en.wikipedia.org/wiki/Unsharp_
##masking) by blurring an image and then subtracting the blurred version from the
##original. This gives a sharpening effect to the image. Try this on both color and
##grayscale images.

infile = '../Images/baboon.png'
sigma = 3
im = np.array(Image.open(infile))
im_blurred = filters.gaussian_filter(im, sigma)
im_unsharp = np.subtract(im_blurred, im)

plt.figure()
plt.imshow(im_unsharp)
plt.title('Unsharp')
plt.show()

