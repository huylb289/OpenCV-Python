import sift
import homography
import warp
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

locationImages = '../Images/pcv_data/data/'
featname = [locationImages + 'Univ' + str(i + 1) + '.sift' for i in range(5)]
imname = [locationImages + 'Univ' + str(i + 1) + '.jpg' for i in range(5)]
l = {}
d = {}

for i in range(5):
    sift.process_image(imname[i], featname[i])
    l[i], d[i] = sift.read_features_from_file(featname[i])

matches = {}
for i in range(4):
    matches[i] = sift.match(d[i+1],d[i])


### function to convert the matches to hom. points
##def convert_points(j):
##    ndx = matches[j].nonzero()[0]
##    fp = homography.make_homog(l[j+1][ndx,:2].T)
##    ndx2 = [int(matches[j][i]) for i in ndx]
##    tp = homography.make_homog(l[j][ndx2,:2].T)
##    return fp,tp
##
### estimate the homographies
##model = homography.RansacModel()
##
##fp,tp = convert_points(0)
##H_01 = homography.H_from_ransac(fp,tp,model)[0] #im 0 to 1
##
##fp,tp = convert_points(1)
##H_12 = homography.H_from_ransac(fp,tp,model)[0] #im 1 to 2
##
##tp,fp = convert_points(2) #NB: reverse order
##H_32 = homography.H_from_ransac(fp,tp,model)[0] #im 3 to 2
##
##tp,fp = convert_points(3) #NB: reverse order
##H_43 = homography.H_from_ransac(fp,tp,model)[0] #im 4 to 3
##
### warp the images
##delta = 2000 # for padding and translation
##im1 = array(Image.open(imname[1]))
##im2 = array(Image.open(imname[2]))
##
##im_12 = warp.panorama(H_12,im1,im2,delta,delta)
##im1 = array(Image.open(imname[0]))
##im_02 = warp.panorama(dot(H_12,H_01),im1,im_12,delta,delta)
##im1 = array(Image.open(imname[3]))
##im_32 = warp.panorama(H_32,im1,im_02,delta,delta)
##im1 = array(Image.open(imname[j+1]))
##im_42 = warp.panorama(dot(H_32,H_43),im1,im_32,delta,2*delta)

def convert_points(j):
  ndx = matches[j].nonzero()[0]
  fp = homography.make_homog(l[j + 1][ndx, :2].T)
  ndx2 = [int(matches[j][i]) for i in ndx]
  tp = homography.make_homog(l[j][ndx2, :2].T)
  return fp, tp

model = homography.RansacModel()

fp, tp = convert_points(1)
H_12 = homography.H_from_ransac(fp, tp, model)[0]
print('12 homogd')

fp, tp = convert_points(0)
H_01 = homography.H_from_ransac(fp, tp, model)[0]
print('01 homogd')

tp, fp = convert_points(2)  # Note: Reversed.
H_32 = homography.H_from_ransac(fp, tp, model)[0]
print('32 homogd')

tp, fp = convert_points(3)  # Note: Reversed.
H_43 = homography.H_from_ransac(fp, tp, model)[0]
print('43 homogd')

# FIXME: Consider using bundle adjustment and Levenberg-Marquardt instead of
# just concatenating homographies which accumulates errors.
delta = 600
H_delta2 = array([[1, 0, -2*delta], [0, 1, 0], [0, 0, 1]])

im1 = array(Image.open(imname[1]))
im2 = array(Image.open(imname[2]))
im_12 = warp.panorama(H_12, im1, im2, delta, delta)
print('12 warpd')

im0 = array(Image.open(imname[0]))
im_02 = warp.panorama(dot(H_12, H_01), im0, im_12, delta, 2*delta)
print('02 warpd')

im3 = array(Image.open(imname[3]))
# There are two images added on the left already, hence the H_delta2.
im_03 = warp.panorama(dot(H_32, H_delta2), im3, im_02, delta, 0)
print('03 warpd')

im4 = array(Image.open(imname[4]))
im_04 = warp.panorama(dot(dot(H_32, H_43), H_delta2), im4, im_03, delta, 0)
print('04 warpd')


# Plot image
plt.figure()
plt.imshow(im_42)
plt.axis('off')
plt.show()
