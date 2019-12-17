import numpy as np
from math import radians, sin
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix


H   = 10.        # height of the hill
V_D = 2_000.     # min distance to village
V_L = 1_000.     # village length
g   = 9.81


def ballistic_eq_check(v_zero, alpha):
    r = v_zero**2 * sin(radians(2*alpha)) / g
    return V_D < r < V_D + V_L



# generate the dataset

x_train = np.empty((100, 2), dtype=np.float32)
x_train[:, 0] = np.random.uniform(100, 200, size=(100,))
x_train[:, 1] = np.random.uniform(30, 60, size=(100,))
y_train = np.vectorize(ballistic_eq_check, otypes=[np.int])(x_train[:, 0], x_train[:, 1])

x_test = np.empty((100, 2), dtype=np.float32)
x_test[:, 0] = np.random.uniform(100, 200, size=(100,))
x_test[:, 1] = np.random.uniform(30, 60, size=(100,))
y_test = np.vectorize(ballistic_eq_check, otypes=[np.int])(x_test[:, 0], x_test[:, 1])


# train the tree




cm = confusion_matrix(y_test, y_test_pred)