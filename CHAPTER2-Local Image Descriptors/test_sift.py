import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt
import os
import sift

imname = 'Yosemite1.jpg'
im1 = np.array(Image.open(imname).convert('L'))
sift.process_image(imname, 'Yosemite1.sift')
l1,d1 = sift.read_features_from_file('Yosemite1.sift')

plt.figure()
plt.gray()
sift.plot_features(im1,l1,circle=True)
plt.show()
