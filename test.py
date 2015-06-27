import os
import numpy
import skimage
import sklearn
import scipy
import scipy.misc

def normalize(arr):
    """
    Linear normalization
    http://en.wikipedia.org/wiki/Normalization_%28image_processing%29
    """
    arr = arr.astype('float')
    # Do not touch the alpha channel
    for i in range(3):
        minval = arr[...,i].min()
        maxval = arr[...,i].max()
        if minval != maxval:
            arr[...,i] -= minval
            arr[...,i] *= (255.0/(maxval-minval))
    return arr

path = "C:\\Users\\anne\\Desktop\\Untitled.png"

image = scipy.misc.imread(path, flatten=0)
new_image = normalize(image)
scipy.misc.imsave("Untitled_test.png", new_image)