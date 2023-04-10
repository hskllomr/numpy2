import numpy as np
A = np.array([[4, -3, 1],[2, 1, 3],[-1, 2, -5]], dtype=np.dtype(float))

b = np.array([-10, 0, 17], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

x = np.linalg.solve(A, b)

print(f"Solution: {x}")

d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")

A_system = np.hstack((A, b.reshape((3, 1))))

print(A_system)

#****************************************************************************************
import numpy as np
A = np.array([[4, -3, 1],[2, 1, 3],[-1, 2, -5]], dtype=np.dtype(float))

b = np.array([-10, 0, 17], dtype=np.dtype(float))

A_system = np.hstack((A, b.reshape((3, 1))))

def MultiplyRow(M, row_num, row_num_multiple):
    M_new = M.copy()
    M_new[row_num] = M_new[row_num] * row_num_multiple
    return M_new

print("Original matrix:")
print(A_system)
print("\nMatrix after its third row is multiplied by 2:")
print(MultiplyRow(A_system,2,2))

#****************************************************************************************

import numpy as np
A = np.array([[4, -3, 1],[2, 1, 3],[-1, 2, -5]], dtype=np.dtype(float))

b = np.array([-10, 0, 17], dtype=np.dtype(float))

A_system = np.hstack((A, b.reshape((3, 1))))

def AddRows(M, row_num_1, row_num_2, row_num_1_multiple):
    M_new = M.copy()
    M_new[row_num_2] = row_num_1_multiple * M_new[row_num_1] + M_new[row_num_2]
    return M_new

print("Original matrix:")
print(A_system)
print("\nMatrix after exchange of the third row with the sum of itself and second row multiplied by 1/2:")
print(AddRows(A_system,1,2,1/2))

#****************************************************************************************
import numpy as np
A = np.array([[4, -3, 1],[2, 1, 3],[-1, 2, -5]], dtype=np.dtype(float))

b = np.array([-10, 0, 17], dtype=np.dtype(float))

A_system = np.hstack((A, b.reshape((3, 1))))

def SwapRows(M, row_num_1, row_num_2):
    M_new = M.copy()
    M_new[[row_num_1, row_num_2]] = M_new[[row_num_2, row_num_1]]
    return M_new

print("Original matrix:")
print(A_system)
print("\nMatrix after exchange its first and third rows:")
print(SwapRows(A_system,0,2))

#****************************************************************************************
