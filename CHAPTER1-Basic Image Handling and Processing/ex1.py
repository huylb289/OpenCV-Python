from PIL import Image
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt

##1. Take an image and apply Gaussian blur like in Figure 1-9. Plot the image contours
##for increasing values of σ . What happens? Can you explain why?

##Answer:
##    Image go blurrer with sigma increase


infile = '../Images/frog.jpg'
sigma = 1

for i in range(5):
    sigma = i
    im = np.array(Image.open(infile))
    im2 = filters.gaussian_filter(im, sigma)
    plt.figure()
    plt.imshow(im2)
    plt.title('Frog gaussian:'+str(i))

plt.show()
