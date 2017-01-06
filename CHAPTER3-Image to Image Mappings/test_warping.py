import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import homography
from scipy import ndimage
import warp

# example of affine warp of im1 onto im2
im1 = np.array(Image.open('../Images/beatles.jpg').convert('L'))
im2 = np.array(Image.open('../Images/billboard_for_rent.jpg').convert('L'))

# set to points
##tp = np.array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])
tp = np.array([[675,826,826,677],[55,52,281,277],[1,1,1,1]])
im3 = warp.image_in_image(im1,im2,tp)

##plt.figure()
##plt.gray()
##plt.imshow(im3)
##plt.axis('equal')
##plt.axis('off')
##plt.show()

# set from points to corners of im1
m, n = im1.shape[:2]
fp = np.array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])

# first triangle
tp2 = tp[:,:3]
fp2 = fp[:,:3]

# compute H
H = homography.Haffine_from_points(tp2,fp2)
im1_t = ndimage.affine_transform(im1,H[:2,:2],\
                                 (H[0,2],H[1,2]),im2.shape[:2])

# alpha for triangle
alpha = warp.alpha_for_triangle(tp2, im2.shape[0],im2.shape[1])
im3 = (1-alpha)*im2 + alpha*im1_t


# second triangle
tp2 = tp[:,[0,2,3]]
fp2 = fp[:,[0,2,3]]

# compute H
H = homography.Haffine_from_points(tp2, fp2)
im1_t = ndimage.affine_transform(im1, H[:2,:2],\
                                 (H[0,2],H[1,2]),im2.shape[:2])

# alpha for triangle
alpha = warp.alpha_for_triangle(tp2, im2.shape[0],im2.shape[1])
im4 = (1-alpha)*im3 + alpha*im1_t

plt.figure()
plt.gray()
plt.imshow(im4)
plt.axis('equal')
plt.axis('off')
plt.show()
