from PIL import Image
from numpy import *
from scipy.ndimage import filters
import matplotlib.pyplot as plt

infile = '../Images/frog.jpg'
sigma = 5
im = array(Image.open(infile))
im2 = filters.gaussian_filter(im, sigma)

plt.figure()
plt.imshow(im2)
plt.title('Frog gaussian')


# Blur increasing sigma
im = array(Image.open(infile))
im2 = zeros(im.shape)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = uint8(im2)

plt.figure()
plt.imshow(im2)
plt.title('Frog gaussian')
plt.show()

