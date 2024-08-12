import numpy as np

n = input('Enter the number of points (positive integer): ')

assert n.isdigit(), 'Please enter a positive integer.'

k = input('Enter the value for k (number of neighbors): ')

assert k.isdigit(), 'Please enter a positive integer.'
assert k <= n, 'The value of k must be less than or equal to the number of points.'

x_ = np.zeros(int(n))
y_ = np.zeros(int(n))

for i in range(int(n)):
    x = input(f'Enter the x-coordinate for point {i+1}: ')
    y = input(f'Enter the y-coordinate for point {i+1}: ')
    x_[i] = x
    y_[i] = y

# provide x and y as vectors
def knn_regr(x, y, k, x_new):
    # calculate the Euclidean distance between x_new and each point in x
    dist = np.sqrt((x - x_new)**2)
    # sort the distances in ascending order and get the indices
    idx = np.argsort(dist)
    # get the k nearest neighbors
    y_knn = y[idx[:k]]
    # return the mean of the k nearest neighbors
    return np.mean(y_knn)


x_test = input('Enter the x-coordinate for the test point: ')
y_pred = knn_regr(x_, y_, int(k), float(x_test))
print(f'The predicted y-coordinate for the test point is: {y_pred}')