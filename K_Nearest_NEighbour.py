import numpy as np 
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace =True)
df.drop(['id'],1,inplace = True)

X = np.array(df.drop(['class']))
y = np.array(df['class'])