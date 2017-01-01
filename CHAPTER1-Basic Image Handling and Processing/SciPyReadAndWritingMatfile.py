from PIL import Image
from numpy import *
from scipy.ndimage import measurements, morphology
from scipy import io
from scipy.misc import imsave
import scipy
import matplotlib.pyplot as plt

# Load data from mat file
file_mat = './test_mat.mat'
data = io.loadmat(file_mat)


# Save data into mat file
data = {}
data['x'] = 'this is some string'
io.savemat('test.mat',data)

# Load image from library
im = scipy.misc.ascent()

# Saving arrays as images
imsave('test_imsave.jpg', im)
