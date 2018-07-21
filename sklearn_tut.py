from sklearn.model_selection import train_test_split
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target
print(len(iris.target), len(iris.data))
print(y)

print(iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier