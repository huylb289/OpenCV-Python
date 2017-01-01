from PIL import Image
from numpy import *
from scipy.ndimage import measurements, morphology
import matplotlib.pyplot as plt


# Load image and threshold to make sure it is binary
infile = '../Images/girl.png'
im = array(Image.open(infile).convert('L'))
im = 1*(im<128)

plt.figure()
plt.imshow(im)

labels, nbr_objects = measurements.label(im)
print ("Number of objects:", nbr_objects)


# morphology - opening to separate object better
im_open = morphology.binary_opening(im, ones((9,5)), iterations=2)

labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)

plt.show()
