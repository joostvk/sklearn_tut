
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from scipy.spatial import distance

def euc(a, b):
    """
    :param a: locatie a
    :param b: locatie b
    :return:  euclidean distance between a and b
    """
    return distance.euclidean(a, b)


euc((0, 0), (1, 1))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

import random

class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best = euc()

