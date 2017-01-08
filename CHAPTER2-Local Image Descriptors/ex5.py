import harris
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sift


##5. The VLFeat command line tools also contain an implementation of Maximally
##Stable Extremal Regions (MSER) ( http://en.wikipedia.org/wiki/Maximally_stable_
##extremal_regions) a region detector that finds blob-like regions. Create a function
##for extracting MSER regions and pass them to the descriptor part of SIFT using the
##--read-frames option and one function for plotting the ellipse regions.

