import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt
import rof
import harris

##2. Incrementally apply stronger blur (or ROF de-noising) to an image and extract
##Harris corners. What happens?

# Gaussian blurred: cannot detect corner by a big sigma
# Denoise: still have corner


#create synthetic image with noise
im = np.array(Image.open('./Yosemite1.jpg').convert('L'))
im_blurred = filters.gaussian_filter(im,10)
U,T = rof.denoise(im,im)

# Apply Harris conner detector on Gaussian Blurred Image
harrisim = harris.compute_harris_response(im_blurred)
filtered_coords = harris.get_harris_points(harrisim,6,0.2)
harris.plot_harris_points(im_blurred, filtered_coords)

# Apply Harris conner detector on Denoise
harrisim = harris.compute_harris_response(U)
filtered_coords = harris.get_harris_points(harrisim,6,0.2)
harris.plot_harris_points(U, filtered_coords)

plt.show()



# save the result
from scipy.misc import imsave

imsave('synth_rof.pdf',U)
imsave('synth_gaussian.pdf',im_blurred)


