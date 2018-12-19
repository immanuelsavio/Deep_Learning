from math import sqrt
import numpy as np
import warnings
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k' : [[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]] }
new_feature = [5,7]

#for i in dataset:
#   for ii in dataset[i]:
#      [plt.scatter(ii[0],ii[1], s=100, color=i)]
#plt.scatter(new_feature[0],new_feature[1])
#plt.show()

def k_nearest_neighbours(data, predict, k=3):
    if len(data) >=k:
        warnings.warn('K is set a value less than voting')
    distances = []
    for group in data:
        for features in data[group]: 
            eucl_dist = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([eucl_dist,group])
    votes = [i[1] for i in sorted(distances) [:k]]
    else:    
        return vote_result  
