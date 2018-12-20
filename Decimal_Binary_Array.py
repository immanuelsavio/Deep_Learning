import numpy as np 
import random

a = []
for i in range (0,1024):
    num = i
    x = np.binary_repr(i, width = 10) 
    a.append([int(i) for i in str(x)])
np.asarray(a)

x = []
for i in range(5):
        x.append(int(random.randrange(1024)))

data = []
for i in x:
    data.append(a[i])

train = [data[i] for i in range(4)]
test = [data[4]]

print(train)
print(test)