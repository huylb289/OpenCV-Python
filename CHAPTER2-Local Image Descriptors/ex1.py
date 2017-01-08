import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt

##1. Modify the function for matching Harris corner points to also take a maximum
##pixel distance between points for them to be considered as correspondences, in
##order to make matching more robust.


##Old function matching
def match(desc1, desc2, threshold=0.5):
    """ For each corner point descriptor in the first image,
    select its match to second image using
    normalized cross-correlation. """

    n = len(desc1[0])

    # pair-wise distances
    d = - np.ones((len(desc1),len(desc2)))
    for i in range(len(desc1)):
        for j in range(len(desc2)):
            d1 = (desc1[i] - np.mean(desc1[i])) / np.std(desc1[i])
            d2 = (desc2[j] - np.mean(desc2[j])) / np.std(desc2[j])
            ncc_value = np.sum(d1 * d2) / (n-1)
            if ncc_value > threshold:
                d[i,j] = ncc_value

    # sort DESC
    ndx = np.argsort(-d)
    matchscores = ndx[:,0]

    return matchscores

##New function: we need to define the maximum pixel distance between points for them
##to be consedered as correspondences
def match(desc1, desc2, threshold=0.5, maximumPixelDistance=5):
    """ For each corner point descriptor in the first image,
    select its match to second image using
    normalized cross-correlation. """

    n = len(desc1[0])

    # pair-wise distances
    d = - np.ones((len(desc1),len(desc2)))
    for i in range(len(desc1)):
        # Create -5 -4 -3 -2 -1 0 1 2 3 4 range distance
        for j in range(i - maximumPixelDistance, i + maximumPixelDistance, 1):
            try:
                d1 = (desc1[i] - np.mean(desc1[i])) / np.std(desc1[i])
                d2 = (desc2[j] - np.mean(desc2[j])) / np.std(desc2[j])
                ncc_value = np.sum(d1 * d2) / (n-1)
                if ncc_value > threshold:
                    d[i,j] = ncc_value
            except IndexError:
                print ("Some index error")
                continue

    # sort DESC
    ndx = np.argsort(-d)
    matchscores = ndx[:,0]

    return matchscores


