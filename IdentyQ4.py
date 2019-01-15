
#Question4:
import numpy as np
array = np.random.randint(100, size = 10)
for i in range(0,len(array)):
    if (i+1)%2 == 0:
           array[i] = -10
print(array)

