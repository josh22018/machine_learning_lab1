import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

def trans(a):
    transpose = []
    sha = a.shape
    first = sha[0]
    sec = sha[1]
    for i in range(sec):  # Loop over columns instead of rows
        row = []  # Create a new row for the transpose
        for j in range(first):
            row.append(a[j][i])
        transpose.append(row)
    return np.array(transpose)

print("Original Matrix")
print(a)
print("Transpose")
print(trans(a))
