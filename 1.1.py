# matrix multiplication.
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[9, 2], [4, 5],[2,3]])
def mult(a,b):
    first=a.shape
    second=b.shape
    if len(first)==len(second) and first[1] == second[0]:
        return np.dot(a, b)
    else:
        print("error the dimensions are not matching.")
print(mult(a,b))