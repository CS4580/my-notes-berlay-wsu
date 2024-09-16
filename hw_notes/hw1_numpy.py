import numpy as np
import time

# Create a Python list with integers from 1 to 1 000 000
oneMillion = [num for num in range(1, int(1e6)+1)]

# Time the execution of addition operation on the list
start_time = time.time()
list = [i + 10 for i in oneMillion]
end_time = time.time()

# Print the execution time
print('Execution time for list (seconds): ', end_time - start_time)

# Create the array
array = np.array(oneMillion)

# Time the execution of addition operation on the array
start_time = time.time()
array = array + 10
end_time = time.time()

# Print the execution time
print('Execution time for array (seconds): ', end_time - start_time)

## Ndarray Attributes

# Create an ndarray using np.array
arr_2d = np.array([[2, 7 ,6],[5,4, 9]])

# Print the array
print(f'2D Array:\n {arr_2d}')

# Print the shape of the array
print(f'Shape: {arr_2d.shape}' )

# Print the size of the array
print(f'Size: {arr_2d.size}')

# Print the number of dimensions of the array
print(f'Number of dimensions: {arr_2d.ndim}')

# Print the data type of the elements in the array
print(f'Type: {arr_2d.dtype}')