import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt
import os
import sift

imname1 = 'Yosemite1.jpg'
imname2 = 'Yosemite2.jpg'

im1 = np.array(Image.open(imname1).convert('L'))
sift.process_image(imname1, 'Yosemite1.sift')
l1,d1 = sift.read_features_from_file('Yosemite1.sift')

im2 = np.array(Image.open(imname2).convert('L'))
sift.process_image(imname2, 'Yosemite2.sift')
l2,d2 = sift.read_features_from_file('Yosemite2.sift')

plt.figure()
plt.gray()
sift.plot_features(im1,l1,circle=True)

plt.figure()
plt.gray()
sift.plot_features(im2,l2,circle=True)

print ('starting matching')
matches = sift.match_twosided(d1,d2)
print ('{} matches'.format(len(matches.nonzero()[0])))

plt.figure()
plt.gray()
sift.plot_matches(im1,im2,l1,l2,matches, show_below=True)

plt.show()


