from math import sqrt
import numpy as np
import warnings
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k' : [[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]] }
new_feature = [5,7]

plt.scatter