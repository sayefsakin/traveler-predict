import numpy as np


def get_user_label(s):
    stdv = np.std(s, dtype=np.float64)
    if stdv > 20:
        return 1
    elif 0 < stdv < 4:
        return -1
    else:
        return 0


def assign_user_label(sample, d):
    labeled_samples = []
    for i, s in enumerate(sample):
        lab = get_user_label(s)
        labeled_samples.append({'features': s, 'label': lab, 'time': d[i][1]})
    return np.array(labeled_samples)
