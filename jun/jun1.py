import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sample_memo = 'Milt, were gonna need to go ahead and a a move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?'
a = sample_memo.split(" ")
b = a.index('a')

names1=['num','month']
data = pd.read_table('E:/zheda/project/disease/jun/jun1.txt',header=None,encoding='utf-8',sep='\s+',names=names1)
data1 = data['num']
r=[data1.min(),data1.max(),data1.mean(),data1.std()]
r = pd.DataFrame(r,index=['Min','Max','Mean',"STD"]).T
np.round(r,2)
print r

x =range(0,60)
y = data['num']
plt.plot(x,y)
plt.show()