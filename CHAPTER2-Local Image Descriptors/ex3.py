import harris
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import fast

##3. An alternative corner detector to Harris is the FAST corner detector. There are a
##number of implementations, including a pure Python version available at http://
##www.edwardrosten.com/work/fast.html. Try this detector, play with the sensitivity
##threshold, and compare the corners with the ones from our Harris implementation.

infile = '../Images/Yosemite1.jpg'
resultname = './Yosemite1_fast.jpg'
fast.process_image(infile, resultname, params="-t 50 -n 9")

imresult = np.array(Image.open(resultname))

plt.figure()
plt.imshow(imresult)

im = np.array(Image.open(infile).convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim,6,0.2)
harris.plot_harris_points(im, filtered_coords)
plt.show()
