#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report

def GM11(x0): #自定义灰色预测函数
  import numpy as np
  x1 = x0.cumsum() #1-AGO序列
  z1 = (x1[:len(x1)-1] + x1[1:])/2.0 #紧邻均值（MEAN）生成序列
  z1 = z1.reshape((len(z1),1))
  B = np.append(-z1, np.ones_like(z1), axis = 1)
  Yn = x0[1:].reshape((len(x0)-1, 1))
  [[a],[b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Yn) #计算参数
  f = lambda k: (x0[0]-b/a)*np.exp(-a*(k-1))-(x0[0]-b/a)*np.exp(-a*(k-2)) #还原值
  delta = np.abs(x0 - np.array([f(i) for i in range(1,len(x0)+1)]))
  C = delta.std()/x0.std()
  P = 1.0*(np.abs(delta - delta.mean()) < 0.6745*x0.std()).sum()/len(x0)
  return f, a, b, x0[0], C, P #返回灰色预测函数、a、b、首项、方差比、小残差概率

target = ['0','1']
names1=['month','num']
data = pd.read_table('E:/zheda/project/disease/yigan/yigan3.txt',header=None,encoding='utf-8',sep='\s+',names=names1)
data1 = data['num']
r=[data1.min(),data1.max(),data1.mean(),data1.std()]
r = pd.DataFrame(r,index=['Min','Max','Mean',"STD"]).T
np.round(r,2)
print r

x =range(0,60)
y = data['num']
plt.plot(x,y)
plt.show()

names1=['month','num']
data = pd.read_table('E:/zheda/project/disease/yigan/yigan31.txt',header=None,encoding='utf-8',sep='\s+',names=names1)
data1 = data['num']
r=[data1.min(),data1.max(),data1.mean(),data1.std()]
r = pd.DataFrame(r,index=['Min','Max','Mean',"STD"]).T
np.round(r,2)
print r
x =range(0,60)
y = data['num']
plt.plot(x,y)
plt.show()