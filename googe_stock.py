import pandas as pd 
import quandl 
import math
import numpy as np 
from sklearn import preprocessing, cross_validation,

df = quandl.get('WIKI/GOOGL')
#print(df.head())
df = df [['Adj. Open','Adj. High','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail())