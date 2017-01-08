import harris
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

infile1 = '../Images/opencv-feature-matching-image.jpg'
infile2 = '../Images/opencv-feature-matching-template.jpg'
im1 = np.array(Image.open(infile1).convert('L'))
im2 = np.array(Image.open(infile2).convert('L'))

wid = 5
harrisim = harris.compute_harris_response(im1,5)
filtered_coords1 = harris.get_harris_points(harrisim,wid+1)
d1 = harris.get_descriptors(im1,filtered_coords1,wid)

harrisim = harris.compute_harris_response(im2,5)
filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
d2 = harris.get_descriptors(im2,filtered_coords2,wid)

##print ('starting matching')
##matches = harris.match_twosided(d1,d2,threshold=0.5)
##plt.figure()
##plt.gray()
##harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
##plt.show()


##Testing with maximumPixelDistance
print ('starting matching')
matches = harris.match_twosided(d1,d2,threshold=0.1, maximumPixelDistance=5)
plt.figure()
plt.gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
plt.show()
