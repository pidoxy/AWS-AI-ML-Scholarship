import numpy as np

features = np.array([ 0.49671415, -0.1382643 ,  0.64768854] )
print(features)

print(features.T)

print(features[:, None])

# Alternatively, you can create arrays with two dimensions. Then, you can use arr.T to get the column vector.

np.array(features, ndmin=2)

print(np.array(features, ndmin=2).T)