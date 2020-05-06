from sklearn import svm


class DSAClassifier(object):
    def __init__(self, d, l):
        self.dataset = d
        self.label = l
        self.model = svm.SVC(kernel='rbf')
        self.model.fit(self.dataset, self.label)

    def predictDSA(self, sample):
        return self.model.predict(sample)
