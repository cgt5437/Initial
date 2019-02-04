import math
import random


def distance( point1, point2 ):
    '''
    Returns the Euclidean distance between point1 and point2,
    which are expected to be either tuples or lists of the same length.
    '''
    
    total = 0

    for i in range( len( point1 )):
        diff = point1[i] - point2[i]
        total += diff ** 2

    return math.sqrt( total )

def readFile( filename ):
    '''
    Reads data from a file and returns a dictionary indexed by
    line number (from 1).  Expects data to be one integer per line.
    '''
    datadict = {}

    datafile = open(filename, 'r' )
    values=datafile.readlines()
    key=0
    for i in range(len(values)):
        key=key+1
        lines=values[i].strip().split()
        datadict[key]=int(lines[0]),int(lines[1])
        
        

    datafile.close()
    return datadict

def createCentroids(k, datadict ):
    '''
    Returns a list of k randomly chosen cluster centroids
    from a dictionary.  Requires k <= len( datdict )
    to avoid an infinite loop.
    '''
    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = random.randint(1, len(datadict))
        if rkey not in centroidKeys:
            centroids.append( datadict[rkey] )
            centroidKeys.append(rkey)
            centroidCount += 1

    return centroids

def createClusters( centroids, datadict, repeats ):
    '''
    Creates a set of clusters for a data set.  Parameters are:
     centroids - a list of keys to initial centroids of each cluster
     datadict - a dictionary of key/data pairs
     repeats - an integer specifying how many times to iterate before done
    Returns a list of lists.  In each sublist are the keys that form
    a cluster.
    '''

    # The number of centroids we start with tells us how many
    # clusters we should ultimately have.
    k = len( centroids )

    # We iterate several times, with the idea that the process will
    # converge over time to a set of clusters.
    for apass in range( repeats ):
        # in each pass, the clusters all start off empty
        clusters = []
        for i in range( k ):
            clusters.append([])

        # We compare each value in the data to all of the centroids,
        # and it joins the cluster of the centroid it is closest to.
        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = distance( datadict[akey], centroids[clusterIndex] )
                distances.append(dist)

            mindist = min( distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        # Calculate the new centroid/mean value of each cluster, to
        # use in the next pass.
        dimensions = len( datadict[1] )
        for clusterIndex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                # Sum the x, y, z, etc. coordinates separately
                for ind in range(len(datapoints)):
                    sums[ind] += datapoints[ind]
            # Divide each sum by cluster length to get mean value
            clusterLen = len( clusters[clusterIndex] )
            if clusterLen != 0:
                for ind in range(len(sums)):
                    sums[ind] /= clusterLen

            # sums now contains the mean coordinate point for this cluster
            centroids[clusterIndex] = sums

        ## Debugging code here.  Remove for production code.
        #for c in clusters:
        #    print( "CLUSTER" )
        #    for key in c:
        #        print( datadict[key], end=' ' )
        #    print()

    return clusters
        
