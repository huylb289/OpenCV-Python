import harris
from PIL import Image
import numpy as np

infile = '../Images/Yosemite1.jpg'
im = np.array(Image.open(infile).convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim,6,0.2)
harris.plot_harris_points(im, filtered_coords)
