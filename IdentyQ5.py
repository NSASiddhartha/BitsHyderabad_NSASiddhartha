#Question5:
import numpy as np
list1 = []
array1 = np.random.randint(100, size = 10)
tf = np.array([True, False])
array2 = np.random.choice(tf, len(array1))
for x in range(0,len(array1)):
    if array2[x] is True:
        list1.append(array1[i])
print(array1)
print(array2)
print(list1)

