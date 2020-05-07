#!/usr/bin/env python3
import urllib, json
from urllib.request import urlopen

import numpy as np
from sklearn.cluster import KMeans
from commonUtils import *
from drawing import *
from dsa import compute_dsa
from dsa_classifier import *
from manual_label import *
import sys


def main():
    dr = Drawing()
    bins = 1000
    metric = 'PAPI_TOT_CYC'
    location = 1
    begin = 1242233747#1474043713#416663000
    end = 1664725001#1591763848#1664725001
    _lambda = 0.5
    _gamma = 0.5
    max_iter = 100

    if len(sys.argv) > 1:
        metric = sys.argv[1]
    else:
        print("usage: ./traveler-predict.py <metric> <bins> <begin> <end> <maximum_iterations> <lambda>")
        return
    if len(sys.argv) > 2:
        bins = int(sys.argv[2])
    if len(sys.argv) > 3:
        begin = int(sys.argv[3])
    if len(sys.argv) > 4:
        end = int(sys.argv[4])
    if len(sys.argv) > 5:
        max_iter = int(sys.argv[5])
    if len(sys.argv) > 6:
        _lambda = float(sys.argv[6])


    json_url = urlopen(getUrlString(metric, bins, 1, begin, end))
    location1_data = json.loads(json_url.read())
    d1 = getRateFromList(location1_data)

    json_url = urlopen(getUrlString(metric, bins, 2, begin, end))
    location2_data = json.loads(json_url.read())
    d2 = getRateFromList(location2_data)

    json_url = urlopen(getUrlString(metric, bins, 3, begin, end))
    location3_data = json.loads(json_url.read())
    d3 = getRateFromList(location3_data)

    json_url = urlopen(getUrlString(metric, bins, 4, begin, end))
    location4_data = json.loads(json_url.read())
    d4 = getRateFromList(location4_data)

    json_url = urlopen(getUrlString(metric, bins, 5, begin, end))
    location5_data = json.loads(json_url.read())
    d5 = getRateFromList(location5_data)

    json_url = urlopen(getUrlString(metric, bins, 6, begin, end))
    location6_data = json.loads(json_url.read())
    d6 = getRateFromList(location6_data)

    json_url = urlopen(getUrlString(metric, bins, 7, begin, end))
    location7_data = json.loads(json_url.read())
    d7 = getRateFromList(location7_data)

    json_url = urlopen(getUrlString(metric, bins, 8, begin, end))
    location8_data = json.loads(json_url.read())
    d8 = getRateFromList(location8_data)

    json_url = urlopen(getUrlString(metric, bins, 9, begin, end))
    location9_data = json.loads(json_url.read())
    d9 = getRateFromList(location9_data)

    json_url = urlopen(getUrlString(metric, bins, 10, begin, end))
    location10_data = json.loads(json_url.read())
    d10 = getRateFromList(location10_data)
    #
    darray = np.column_stack((d1, d2, d3, d4, d5, d6, d7, d8, d9, d10))

    labeled_samples = assign_user_label(darray, location4_data)
    compute_dsa(labeled_samples, _lambda, max_iter)
    print("done")
    # dr.plotTimeSeries2(labeled_samples, 'Time Series')
    # c = getDatasetLabel(labeled_samples)
    # dr.plotTimeSeries(location1_data, c, metric)
    # dr.plotTimeSeries(location2_data, c, metric)
    # dr.plotTimeSeries(location3_data, c, metric)

    acc = 0
    for i, d in enumerate(labeled_samples):
        ul = get_user_label(d['features'])
        if d['label'] == 0:
            continue
        if ul == d['label']:
            acc = acc + 1

    print(str(acc / len(labeled_samples)))

if __name__ == '__main__':
    main()
