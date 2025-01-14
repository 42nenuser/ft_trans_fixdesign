import numpy as np  # Standard convention


array = np.array([[10, 20, 30], [40, 50, 60]])

# print(array[0,1])

# print(array[1])

subarray = array[:2, :2]
print(subarray)


array[0, :2] = [99, 88]
print(array)
