import numpy as np

A = np.array([
    [1,2,3],
    [6,4,2],
    [1,7,0],
])

for idx, val in enumerate(A):
    for idx2, val2 in enumerate(val):
        if val2 % 2 == 0:
            val[idx2] = 0
print(A)