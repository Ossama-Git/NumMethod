import numpy as np

m_list = [[2, -1, 1, -1], [2, -1, 0, -3], [3, 0, -1, 1], [2, 2, -2, 5]]
A = np.array(m_list)

inv_A = np.linalg.inv(A)

print(inv_A)

B = np.array([1, 2, -3, -6])
X = np.linalg.inv(A).dot(B)

print(X)

X2 = np.linalg.solve(A,B)

print("the answer is: ")
print(X2)