import numpy as np
from PIL import Image
from scipy.ndimage import filters
import matplotlib.pyplot as plt

def compute_harris_response(im, sigma=3):
    """ Compute the Harris corner detector response function
     for each pixel in grayscale image."""
