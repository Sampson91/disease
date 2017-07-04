#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report

# from sklearn.neural_network import MLPClassifier
target = ['0','1']
names1=['sex1','addrcode','group_id','casetype','age','year']
names2=['sex1','addrcode','group_id','disease_id1','casetype','age','year']
data = pd.read_table('E:/zheda/project/disease/yigan/yigan01.txt',header=None,encoding='utf-8',sep='\s+',names=names2)

r=[data.min(),data.max(),data.mean(),data.std()]
r = pd.DataFrame(r,index=['Min','Max','Mean',"STD"]).T
np.round(r,2)
print r
print np.round(data.corr(method='pearson'),2)
X_trian,X_test,y_train,y_test = train_test_split(data[names2[0:5]],data[names2[6]],test_size=0.3,random_state=42)
clf = DecisionTreeRegressor(max_depth=8,min_samples_split=6)
clf.fit(X_trian,y_train)
tr_predict = clf.predict(X_test)
print(clf.score(X_test,y_test))
# from sklearn.neural_network import MLPClassifier
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15, 5), random_state=1)
# clf.fit(X_trian,y_train)
# tr_predict = clf.predict(X_test)
# print(clf.score(X_test,y_test))
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_trian,y_train)
print(gnb.score(X_test,y_test))
# from sklearn.svm import SVR
# linear_svr = SVR(kernel='linear')
# linear_svr.fit(X_trian,y_train)
# tr_predict = linear_svr.predict(X_test)
# print(linear_svr.score(X_test,y_test))
from sklearn import tree
import pydotplus
dot_data = tree.export_graphviz(clf, out_file=None,feature_names=data[names1[5]],class_names=target,filled=True, rounded=True,special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("E:/zheda/project/disease/yigan/yigan01.pdf")
