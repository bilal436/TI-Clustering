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


path = "C:\\Users\\anne\\PycharmProjects\\DeepLearning\\Project\\Data\\TIWafer\\preprocessed\\images"
Array = []

print "Loading Files ... "

index = 1
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith((".png")):
            # Array.append(scipy.misc.imread(name=name, flatten=0))
            img = scipy.misc.imread(name=os.path.join(root, name), flatten=0)

            image = normalize(img)
            image = image.flatten()
            Array.append(numpy.array(image))
            """
            if not os.path.exists(root+"\\new"):
                os.makedirs(root+"\\new")

            scipy.misc.imsave(os.path.join(root, name), image)
            """
            print "Files Processed : ", index, " out of 16368"
            index += 1

Kmeans = sklearn.cluster.KMeans(n_clusters=8,
                       init='k-means++', n_init=10, max_iter=300,
                       tol=0.0001, precompute_distances='auto',
                       verbose=0, random_state=None, copy_x=True, n_jobs=1)

Clusters = Kmeans.fit(Array)
Clusters = Clusters
