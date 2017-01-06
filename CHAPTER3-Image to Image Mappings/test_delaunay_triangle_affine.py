
import homography
import warp
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

# open image to warp
infile_sunset_tree = '../Images/pcv_data/data/sunset_tree.jpg'
fromim = np.array(Image.open(infile_sunset_tree))
x,y = np.meshgrid(range(5), range(6))
x = (fromim.shape[1]/4) * x.flatten()
y = (fromim.shape[0]/5) * y.flatten()

# triangulate
tri = warp.triangulate_points(x,y)

# open image and description points
im = np.array(Image.open('../Images/pcv_data/data/turningtorso1.jpg'))
tp = np.loadtxt('../Images/pcv_data/data/turningtorso1_points.txt') # destination points

# convert points to hom. coordinates
fp = np.vstack((y,x,np.ones((1,len(x)))))
tp = np.vstack((tp[:,1],tp[:,0],np.ones((1,len(tp)))))

# warp triangles
im = warp.pw_affine(fromim, im, fp, tp, tri)

# plot
plt.figure()
plt.imshow(im)
##plt.figure()
##plt.imshow(im)
##warp.plot_mesh(tp[1],tp[0], tri)
plt.axis('off')
plt.show()
