import statistics
import numpy as np

list = [5,4,3,5,6,7,8,5,4,3]

print('mean', statistics.mean(list))

print('mean', sum(list)/ len(list))

print('median', statistics.median(list))

print('stdev',statistics.stdev(list))

lst = np.array(list)
stdev = np.sqrt(sum((lst - (sum(lst) / len(lst)))**2) / len(lst))
print(stdev)

print('variance',statistics.variance(list))