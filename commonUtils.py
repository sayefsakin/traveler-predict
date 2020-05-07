import numpy as np


def getUrlString(metric, bins, location, begin, end):
    url = 'http://127.0.0.1:8000/datasets/FIB_23_sayef_canvas_gantt/newMetricData?' \
            'bins=' + str(bins) + '&' \
            'location=' + str(location) + '&' \
            'metric_type=' + metric + '&' \
            'begin=' + str(begin) + '&' \
            'end=' + str(end)
    return url


def getRateFromList(lst):
    d = []
    for l in lst:
        d.append(l[2])
    return np.array(d)


def getTimeFromList(lst):
    d = []
    for l in lst:
        d.append(l[1])
    return np.array(d)


def getDatasetTime(dataset):
    d = []
    for l in dataset:
        d.append(l['time'])
    return d


def getDatasetLabel(dataset):
    d = []
    for l in dataset:
        d.append(l['label'])
    return d

def getLocationTitleFromList(lst):
    return 'Location' + str(lst[0][3])