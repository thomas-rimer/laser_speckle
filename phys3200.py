import numpy as np

M_matrix = []
K_columns = 6
N_rows = 6

N = 3

# Create the M matrix
for k in range(0,K_columns): #columns
    M_row = []
    for n in range(0, N_rows):
        M_row.append(np.exp(1j * np.pi * k * n / N))
    M_matrix.append(M_row)

# Take its conjugate
M_conjugate_matrix = []
for row in M_matrix:
    conjugate_row = [np.conjugate(element) for element in row]
    M_conjugate_matrix.append(conjugate_row)

# Convert M_conjugate_matrix to a numpy array
M_conjugate_matrix = np.array(M_conjugate_matrix)

# f_k array
f_k = np.array([[0.0, 1.0/2.0, 1.0, 1.0/2.0, 0, 0]])

# Multiply f_k by the conjugate matrix
f_k_conjugate = np.dot(f_k, M_conjugate_matrix)

for f_element in f_k_conjugate[0]:
    print(f_element.real, f_element.imag)
