#Question2:
import numpy as np
array = np.random.randint(100, size = (5, 4))
print(array)
for i in range(1,5):
    for j in range(1,4):
        if array[i,j] > 50:
            array[i,j] = 100
print(array)


