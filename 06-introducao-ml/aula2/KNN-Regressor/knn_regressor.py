# Based on article:
# https://medium.com/analytics-vidhya/implementing-k-nearest-neighbours-knn-without-using-scikit-learn-3905b4decc3c
import scipy.spatial
from sklearn.model_selection import train_test_split

class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def distance(self, X1, X2):
        distance = scipy.spatial.distance.euclidean(X1, X2)

    def predict(self, X_test, X_train, y_train):
        final_output = []
        for i in range(len(X_test)):
            d = []
            votes = []
            for j in range(len(X_train)):
                dist = scipy.spatial.distance.euclidean(X_train[j] , X_test[i])
                d.append([dist, j])
            d.sort()
            d = d[0:self.k]
            sumk = 0.0
            for d, j in d:
                sumk += y_train[j]
            meank = round(sumk/self.k, 3)
            final_output.append(meank)
        return final_output

    def mse(self, predictions, y_test):
        # predictions = self.predict(X_test, X_train, y_train)
        sum_square = 0.0
        n = len(predictions)
        for i in range(n):
            sum_square += (y_test[i] - predictions[i])**2
        mean_square = sum_square/n
        return mean_square
