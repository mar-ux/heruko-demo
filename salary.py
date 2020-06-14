# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:33:09 2020

@author: smile
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

data=pd.read_csv("hiring.csv")
X=data.iloc[:,:3]
X['experience'].fillna(0,inplace=True)
X['test_score(out of 10)'].fillna(X['test_score(out of 10)'].mean(),inplace=True)
y=data.iloc[:,-1]
def convert_to_int(word):
    word_dict={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]
X['experience']=X['experience'].apply(lambda x :convert_to_int(x))
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(X,y)
pickle.dump(regression,open('model.pkl' ,'wb'))
model=pickle.load(open('model.pkl','rb'))
print(model.predict([[2,9,6]]))