from PIL import Image
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt

# Not complete yet

##Use gradient direction and magnitude to detect lines in an image. Estimate the
##extent of the lines and their parameters. Plot the lines overlaid on the image.

infile = '../Images/baboon.png'
im = np.array(Image.open(infile).convert('L'))
(nr,nc) = im.shape
(dx,dy) = np.gradient(np.double(im))
orientation = np.arctan(np.divide(dx,dy))
(x,y) = np.meshgrid(im.shape[0],im.shape[1])
u = dx
v = dy
plt.figure()
plt.imshow(orientation)
plt.title('Out')
##plt.quiver(x,y,u,v)
plt.show()


# Here
