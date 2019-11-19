import numpy as np

x = np.random.random((5,5))

s= np.mean(x)

d = np.std(x)

z = (x - s)/d

print("Normalized: ", z)