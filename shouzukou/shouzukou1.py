import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names1=['num','month']
data = pd.read_table('E:/zheda/project/disease/shouzukou/shouzukou.txt',header=None,encoding='utf-8',sep='\s+',names=names1)
data1 = data['num']
r=[data1.min(),data1.max(),data1.mean(),data1.std()]
r = pd.DataFrame(r,index=['Min','Max','Mean',"STD"]).T
np.round(r,2)
print r

x =range(0,60)
y = data['num']
plt.plot(x,y)
plt.show()

names1=['num','month']
data = pd.read_table('E:/zheda/project/disease/shouzukou/shouzukou1.txt',header=None,encoding='utf-8',sep='\s+',names=names1)
data1 = data['num']
r=[data1.min(),data1.max(),data1.mean(),data1.std()]
r = pd.DataFrame(r,index=['Min','Max','Mean',"STD"]).T
np.round(r,2)
print r

x =range(0,60)
y = data['num']
plt.plot(x,y)
plt.show()