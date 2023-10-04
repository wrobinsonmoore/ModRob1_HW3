"""
This file was used to answer Question 1 (d, e, f, g) and Question 2!
"""

# Imports
import numpy as np

# Set the numpy print preferences
np.set_printoptions(suppress=True)

# For QUESTION 1. Uncomment if needed!
matrix1 = [[np.cos(-90*np.pi/180), -np.sin(-90*np.pi/180), 0], [np.sin(-90*np.pi/180), np.cos(-90*np.pi/180), 0], [0, 0, 1]]
matrix2 = [[1, 0, 0], [0, np.cos(-90*np.pi/180), -np.sin(-90*np.pi/180)], [0, np.sin(-90*np.pi/180), np.cos(-90*np.pi/180)]]
matrix_result = np.matmul(matrix1, matrix2)

# FOr QUESTION 2. Uncomment if needed!
# p = (1/np.sqrt(3), -1/np.sqrt(6), 1/np.sqrt(2))
# matrixX = [[1, 0, 0], [0, np.cos(30*np.pi/180), -np.sin(30*np.pi/180)], [0, np.sin(30*np.pi/180), np.cos(30*np.pi/180)]]
# matrixY = [[np.cos(135*np.pi/180), 0, np.sin(135*np.pi/180)], [0, 1, 0], [-np.sin(135*np.pi/180), 0, np.cos(135*np.pi/180)]]
# matrixZ = [[np.cos(-120*np.pi/180), -np.sin(-120*np.pi/180), 0], [np.sin(-120*np.pi/180), np.cos(-120*np.pi/180), 0], [0, 0, 1]]
# matrix_result = np.matmul(np.matmul(np.matmul(matrixZ, matrixY), matrixX), p)

# Print the result!
print("Resulting matrix is = ")
print(matrix_result)