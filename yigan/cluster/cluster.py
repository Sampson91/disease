#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report


names1=['card_id','sex1','addrcode','group_id','casetype','age','deadage']

data = pd.read_table('E:/zheda/project/disease/yigan/yigan911.txt',header=None,encoding='utf-8',sep='\s+',names=names1)

data1 = pd.read_table('E:/zheda/project/disease/yigan/yigan92.txt',header=None,encoding='utf-8',sep='\s+',names=names1)
r=[data.min(),data.max(),data.mean(),data.std()]
r = pd.DataFrame(r,index=['Min','Max','Mean',"STD"]).T
np.round(r,2)
print r

import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import MiniBatchKMeans, KMeans
import mpl_toolkits.mplot3d.axes3d as p3
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.datasets.samples_generator import make_blobs
batch_size = 45
mbk = MiniBatchKMeans(init='random', n_clusters=3, batch_size=batch_size,n_init=10, max_no_improvement=10, verbose=0)
# X_trian,X_test,y_train,y_test = train_test_split(data[names1[1:5]],data[names1[6]],test_size=0.3,random_state=42)
X = data[names1[3:6]]

# Y = data[names1[6]]
# Y = Y.fillna(0)
# t0 = time.time()
# mbk.fit(X)
# t_mini_batch = time.time() - t0
# labels= mbk.labels_
# print labels
# la = pd.Series(labels)
# X['y'] = Y
# X['Label'] = la

# X.to_csv("E:/zheda/project/disease/yigan/yigan91.csv")
# X_test =data1[names1[1:5]]
# Y = data1[names1[6]]
# la = mbk.predict(X_test)
# da92 = data1[names1[1:7]]
# da92['Label'] = la
# da92.to_csv("E:/zheda/project/disease/yigan/yigan92.csv")
X = data[names1[3:6]]
st = time.time()
ward = AgglomerativeClustering(n_clusters=6, linkage='ward').fit(X)
elapsed_time = time.time() - st
label = ward.labels_
print("Elapsed time: %.2fs" % elapsed_time)
print("Number of points: %i" % label.size)

fig = plt.figure()
ax = p3.Axes3D(fig)
ax.view_init(7, -80)
X=np.array(X)
for l in np.unique(label):
    a = X[label == l, 0]
    b = X[label == l, 1]
    c = X[label == l, 2]
    ax.plot3D(a, b, c,'o', color=plt.cm.jet(np.float(l) / np.max(label + 1)))
plt.title('Without connectivity constraints (time %.2fs)' % elapsed_time)
plt.show()