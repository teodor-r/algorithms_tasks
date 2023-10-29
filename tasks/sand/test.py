import numpy as np

arr = np.array([53.32, 55.83, 54.37, 53.54, 51.63, 54.58, 54.25, 57.53, 59.85, 60.26])

mean = arr.mean()
std = np.std(arr, ddof=1)
n =10
std_ex = 1.35
u_ex = 55.2
r = 0.61
u_1 = (n* mean/ std**2 + u_ex/ std_ex**2)/ (n/std**2 + 1/std_ex**2)

K = np.array([[1, 0.61],[0.61, 1]]) * std_ex**2

result = np.linalg.inv (K)

print(u_1)
print(K)
print(result)
