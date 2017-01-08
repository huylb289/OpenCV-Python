from PIL import Image
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt

##An alternative image normalization to histogram equalization is a quotient image. A
##quotient image is obtained by dividing the image with a blurred version I /(I ∗ G σ ).
##Implement this and try it on some sample images.

infile = '../Images/baboon.png'
sigma = 3
im = np.array(Image.open(infile))
im_blurred = filters.gaussian_filter(im, sigma)
im_quotient = np.subtract(im, im_blurred)

plt.figure()
plt.imshow(im_quotient)
plt.title('Quotient')
plt.show()
