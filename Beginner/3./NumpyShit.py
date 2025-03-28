import numpy as np 

a = np.array([1,2,3,4,5])

print(a)

b = np.random.randint(0,100, size = (3,3))

print(b)

print(f"median: {np.median(b)}")
print(f"mean: {np.mean(b)}")
print(f"sum: {np.sum(b)}")