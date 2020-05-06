import urllib, json
from urllib.request import urlopen

import numpy as np
from sklearn.cluster import KMeans
from commonUtils import *
from drawing import *
from dsa import compute_dsa
from dsa_classifier import *
from manual_label import *


def runKMeans(sample, n_clusters, dr):
    number_of_clusters = n_clusters
    Kmean = KMeans(n_clusters=number_of_clusters)
    Kmean.fit(sample)
    dr.plotSampleIn3D(['location1', 'location2', 'location3'], sample[:, 0], sample[:, 1], sample[:, 2])
    # print(Kmean.cluster_centers_)
    # # print(Kmean.labels_)
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(sample[:, 0], sample[:, 1], sample[:, 2])
    # for i in range(number_of_clusters):
    #     ax.scatter(Kmean.cluster_centers_[i][0], Kmean.cluster_centers_[i][1], Kmean.cluster_centers_[i][2], s=100, marker='s')
    # ax.scatter(Kmean.cluster_centers_[1][0], Kmean.cluster_centers_[1][1], Kmean.cluster_centers_[1][2], s=100, c='r', marker='s')
    # ax.scatter(Kmean.cluster_centers_[2][0], Kmean.cluster_centers_[2][1], Kmean.cluster_centers_[2][2], s=100, c='b', marker='s')
    # plt.show()
    return Kmean.labels_


def main():
    dr = Drawing()
    bins = 1000
    metric = 'PAPI_TOT_CYC'
    location = 1
    begin = 1242233747#1474043713#416663000
    end = 1664725001#1591763848#1664725001
    number_of_clusters = 5

    json_url = urlopen(getUrlString(bins, 1, begin, end))
    location1_data = json.loads(json_url.read())
    d1 = getRateFromList(location1_data)

    json_url = urlopen(getUrlString(bins, 2, begin, end))
    location2_data = json.loads(json_url.read())
    d2 = getRateFromList(location2_data)

    json_url = urlopen(getUrlString(bins, 3, begin, end))
    location3_data = json.loads(json_url.read())
    d3 = getRateFromList(location3_data)

    json_url = urlopen(getUrlString(bins, 4, begin, end))
    location4_data = json.loads(json_url.read())
    d4 = getRateFromList(location4_data)
    #
    darray = np.column_stack((d1, d2, d3, d4))
    # # plotSampleIn2D(['location1', 'location2'], d1, d2)
    # # plotSampleIn3D(['location1', 'location2', 'location3'], d1, d2, d3)
    # c = runKMeans(darray, number_of_clusters, dr)
    # dr.plotTimeSeries(location1_data, c, metric)
    # dr.plotTimeSeries(location2_data, c, metric)
    # dr.plotTimeSeries(location3_data, c, metric)
    # # plotTimeSeries(location4_data, c, metric)
    # # complete_label(darray)

    # dsaC = DSAClassifier([[0, 0, 0], [1, 1, 0], [0, 1, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [10, 10, 0], [10, 11, 0], [11, 12, 0]], [-1, -1, -1, -1, -1, -1, 1, 1, 1])
    # print(dsaC.predictDSA([[5., 5., 0.]]))
    # # print(dsaC.model.support_vectors_)
    labeled_samples = assign_user_label(darray)
    _lambda = 0.60
    _gamma = 0.5
    max_iter = 100
    compute_dsa(labeled_samples, _lambda, _gamma, max_iter)

if __name__ == '__main__':
    main()
