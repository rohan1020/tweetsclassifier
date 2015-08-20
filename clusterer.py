class Clusterer():
    """
    Parent class for all clustering algo implementations.
    """
    pass



from sklearn.cluster import KMeans, MiniBatchKMeans

class K_Means(Clusterer):
    """
    K-Means clusterning algo implementation
    """

    
    def cluster(X, k):
        """
        Input: Unlabelled dataset and k for k-means 
        Output: List of k clusters
        """
        km = KMeans(
                n_clusters=k, 
                init='k-means++', 
                max_iter=100, 
                n_init=1,
                verbose=True
                )

        km.fit(X)

        return km.labels_
