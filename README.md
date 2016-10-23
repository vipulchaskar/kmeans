# k-means algorithm
Python implementation of k-means clustering algorithm with graphs created with matplotlib.

## How it works
Run the program as "python kmeans.py". It opens and reads data from a file "input.txt" which is in the same directory.
It shows this data on a 2D scatterplot to the user. Then it accepts number of clusters to create (k) and begins running the k-means algorithm.
After it finishes execution, it shows a similar 2D plot but with points color coded based on the cluster they belong to.
It will also show the corresponding cluster centres for each cluster - in its unique color.

As of now, the implementation is limited to 2 features in the input data i.e. 2 dimensional training sets.

## Screenshots

## Requirements
* Python 2.7.x
* Library - matplotlib
* Library - numpy
