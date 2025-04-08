import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("NumPy array:", arr)

# Performing operations on the array
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))

# Reshaping the array
reshaped_arr = arr.reshape(5, 1)
print("Reshaped array:\n", reshaped_arr)

# Slicing the array
sliced_arr = arr[1:4]
print("Sliced array:", sliced_arr)

# Performing element-wise operations
arr2 = np.array([6, 7, 8, 9, 10])
print("Addition:", arr + arr2)
print("Multiplication:", arr * arr2)