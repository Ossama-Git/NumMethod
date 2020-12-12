import numpy as np

m_list = [[1, -1, -1, 1], [2, -1, 3, -2], [0, 1, -1, 2], [3, -1, 1, -1]]
A = np.array(m_list)

inv_A = np.linalg.inv(A)

print(inv_A)

B = np.array([4, 1, 6, 0])
X = np.linalg.inv(A).dot(B)

print(X)

X2 = np.linalg.solve(A,B)

print("the answer is: ")
print(X2)