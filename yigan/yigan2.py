#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report

# from sklearn.neural_network import MLPClassifier

names1=['sex1','addrcode','group_id','casetype','age','year']
names2=['sex1','addrcode','group_id','disease_id1','casetype','age','year']
data = pd.read_table('E:/zheda/project/disease/yigan/yigan02.txt',header=None,encoding='utf-8',sep='\s+',names=names1)
# target = data.drop_duplicates('year')['year']
target = ['2006','2007','2008','2009','2010']

X_trian,X_test,y_train,y_test = train_test_split(data[names1[0:4]],data[names1[5]],test_size=0.3,random_state=42)
clf = DecisionTreeRegressor(max_depth=8,min_samples_split=6)
clf.fit(X_trian,y_train)
tr_predict = clf.predict(X_test)

print(clf.score(X_test,y_test))

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15, 5), random_state=1)
clf.fit(X_trian,y_train)
tr_predict = clf.predict(X_test)
print(clf.score(X_test,y_test))
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_trian,y_train)

tr_predict = gnb.predict(X_test)
print(classification_report(y_test,tr_predict,target_names=target))
print(gnb.score(X_test,y_test))



