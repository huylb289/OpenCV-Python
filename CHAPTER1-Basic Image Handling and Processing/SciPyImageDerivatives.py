from PIL import Image
from numpy import *
from scipy.ndimage import filters
import matplotlib.pyplot as plt


infile = '../Images/airplane.png'
im = array(Image.open(infile).convert('L'))

###Sobel derivative filters
##imx = zeros(im.shape)
##filters.sobel(im,1,imx)
##
##imy = zeros(im.shape)
##filters.sobel(im,0,imy)
##
### Calculate magnitude
##magnitude = sqrt(imx**2 + imy**2)


# Gaussian filter
sigma = 5 # standard deviation
im_gx = zeros(im.shape)
filters.gaussian_filter(im,(sigma,sigma),(0,1), im_gx)

im_gy = zeros(im.shape)
filters.gaussian_filter(im,(sigma,sigma),(1,0), im_gy)

# Calculate magnitude
magnitude_g = sqrt(im_gx**2 + im_gy**2)

plt.figure()
plt.imshow(im)

plt.figure()
plt.imshow(im_gx)

plt.figure()
plt.imshow(im_gy)

plt.figure()
plt.imshow(magnitude_g)

plt.show()
