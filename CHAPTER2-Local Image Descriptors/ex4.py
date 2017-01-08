import harris
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sift

##4. Create copies of an image with different resolutions (for example, by halving the
##size a few times). Extract SIFT features for each image. Plot and match features to
##get a feel for how and when the scale independence breaks down.

infile = '../Images/Yosemite1.jpg'
imOriginal = np.array(Image.open(infile))
sizeOriginal = imOriginal.shape

reduceTime = 4
resizeRow = int(sizeOriginal[0]/reduceTime)
resizeCol = int(sizeOriginal[1]/reduceTime)
resize = resizeCol, resizeRow
outfile = './Yosemite1_resize.jpg'
imHalv = Image.open(infile).resize(resize)
imHalv.save(outfile)
imHalv = np.array(imHalv)

##plt.figure()
##plt.title('Original')
##plt.imshow(imOriginal)
##
##plt.figure()
##plt.title('Halve size')
##plt.imshow(imHalv)


##Process Sift
imname1 = infile
imname2 = outfile

im1 = imOriginal
sift.process_image(imname1, 'Yosemite1.sift')
l1,d1 = sift.read_features_from_file('Yosemite1.sift')

im2 = imHalv
sift.process_image(imname2, 'Yosemite2.sift')
l2,d2 = sift.read_features_from_file('Yosemite2.sift')

plt.figure()
plt.gray()
sift.plot_features(im1,l1,circle=True)

plt.figure()
plt.gray()
sift.plot_features(im2,l2,circle=True)

plt.show()

