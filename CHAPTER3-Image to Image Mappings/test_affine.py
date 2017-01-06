import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import homography
from scipy import ndimage

infile = '../Images/boat.png'
im = np.array(Image.open(infile).convert('L'))
H = np.array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im2 = ndimage.affine_transform(im,H[:2,:2],(H[0,2],H[1,2]))

plt.figure()
plt.gray()
plt.imshow(im2)
plt.show()



