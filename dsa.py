import random

import numpy as np

from convex_polytop import in_hull
from dsa_classifier import *
from manual_label import get_user_label


def isInPositiveRegion(points, x):
    return in_hull(np.array(points), x)


def isInNegativeRegion(points, x):
    return in_hull(np.array(points), x)


def calculate_accuracy(d_plus, d_u):
    den = len(d_plus) + len(d_u)
    return len(d_plus) / den


def compute_dsa(D, _lambda, _gamma, max_iter):
    def getFeatureList(dataset):
        fet = []
        for ei in dataset:
            fet.append(D[ei]['features'])
        return np.array(fet)

    def getLabelList(dataset):
        lab = []
        for ei in dataset:
            lab.append(D[ei]['label'])
        return np.array(lab)

    D_eval = D
    R_plus = []
    R_minus = []
    D_plus = []
    D_minus = []
    D_u = []
    for i in range(len(D_eval)):
        D_u.append(i)
    D_labeled = []
    D_unlabeled = []
    D_labeled_by_user = []
    poolSize = 10
    for i, d in enumerate(D):
        if d['label'] != 0:
            D_labeled_by_user.append(i) #it is D_label in the text, but D_label isnt use anywhere below
        else:
            D_unlabeled.append(i)
    D_labeled_by_dsm = []
    epoch = 0

    while True:
        for i in D_labeled_by_user:
            if D[i]['label'] == 1:
                R_plus.append(D[i]['features'])
            else:
                R_minus.append(D[i]['features'])

        temp = []
        while D_u:
            i = D_u.pop()
            if len(R_plus) > 0 and isInPositiveRegion(R_plus, D[i]['features']):
                D[i]['label'] = 1
                D_plus.append(i)
            elif len(R_minus) > 0 and isInNegativeRegion(R_minus, D[i]['features']):
                D[i]['label'] = -1
                D_minus.append(i)
            else:
                temp.append(i)
        while temp:
            D_u.append(temp.pop())

        accuracy = calculate_accuracy(D_plus, D_u)

        for d in D_labeled_by_user:
            D_labeled.append(d)
        for d in D_labeled_by_dsm:
            D_labeled.append(d)

        for d in D_labeled_by_user:
            if d in D_unlabeled:
                D_unlabeled.remove(d)
        for d in D_labeled_by_dsm:
            if d in D_unlabeled:
                D_unlabeled.remove(d)

        # train classifier
        classifier = DSAClassifier(getFeatureList(D_labeled), getLabelList(D_labeled))
        D_labeled_by_user = []
        D_labeled_by_dsm = []

        # if random.uniform(0.0, 1.0) <= _gamma:
        #     ind = 0
        #     for i in D_u:
        #         D[i]['label'] = get_user_label(D[i]['features'])
        #         D_labeled_by_user.append(i)
        #         ind = ind + 1
        #         if ind > poolSize:
        #             break
        # else:
        ind = 0
        for i in D_unlabeled:
            x = classifier.predictDSA(np.array([D[i]['features']]))
            # print(x[0])
            D[i]['label'] = x[0]
            D_labeled_by_dsm.append(i)
            ind = ind + 1
            if ind > poolSize:
                break
        print("\rEpoch: " + str(epoch) + " Accuracy: " + str(accuracy), end='')
        epoch = epoch + 1
        if epoch >= max_iter or accuracy >= _lambda:
            break
