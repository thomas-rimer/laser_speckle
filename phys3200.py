import numpy as np
import matplotlib.pyplot as plt

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

f_k_conjugate = 1.0/6.0 * f_k_conjugate

for f_element in f_k_conjugate[0]:
    print(f_element.real, f_element.imag)

# Plot the values
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(f_k_conjugate[0].real, marker='o', label='Real Part')  # Add color='blue' to the plot
plt.axhline(y=0, color='black', linestyle='--')  # Add horizontal tick line at y=0
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(f_k_conjugate[0].imag, marker='o', label='Imaginary Part', color='orange')
plt.axhline(y=0, color='black', linestyle='--')  # Add horizontal tick line at y=0

plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.tight_layout()
plt.show()