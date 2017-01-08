from PIL import Image
import numpy as np
from scipy.ndimage import filters
import matplotlib.pyplot as plt
from scipy.ndimage import measurements, morphology, label

##Experiment with successive morphological operations on a thresholded image of
##your choice. When you have found some settings that produce good results, try the
##function center_of_mass in morphology to find the center coordinates of each object
##and plot them in the image.

# Load image and threshold to make sure it is binary
infile = '../Images/pcv_data/data/houses.png'
im = np.array(Image.open(infile).convert('L'))
im = 1*(im<128)

labels, nbr_objects = measurements.label(im)
print ("Number of objects:", nbr_objects)

# morphology - opening to separate object better
im_open = morphology.binary_opening(im, np.ones((9,5)), iterations=4)

labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)

lbl = label(im_open)[0]
list_center_mass = measurements.center_of_mass(im_open, lbl, range(1,nbr_objects_open))
print ("list_center_mass:", list_center_mass)

plt.figure()
plt.imshow(im_open)

for item in list_center_mass:
    plt.plot(item[0], item[1],'ro')

plt.show()
