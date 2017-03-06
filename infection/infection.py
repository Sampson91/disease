import pandas as pd

# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# from sklearn.neural_network import MLPClassifier
target = ['0','1']
names=['sex','addrcode','group_id','casetype','disese_id1','diagnosedate','age','death']
data = pd.read_table('E:/zheda/project/disease/infection/disease61.txt',header=None,encoding='utf-8',sep='\s+',names=['sex','addrcode','group_id','casetype','disese_id1','diagnosedate','age','death'])
data.to_csv("E:/zheda/project/disease/infection/disease3.csv")
X_trian,X_test,y_train,y_test = train_test_split(data[names[0:6]],data[names[7]],test_size=0.3,random_state=42)

clf = DecisionTreeClassifier(max_depth=6,min_samples_split=6)
clf.fit(X_trian,y_train)
# data1 = pd.read_table('E:/zheda/project/disease/infection/disease57.txt',header=None,encoding='utf-8',sep='\s+',names=['sex','addrcode','group_id','casetype','disese_id1','diagnosedate','age','death'])
# X_trian1,X_test1,y_train1,y_test1 = train_test_split(data1[names[0:6]],data1[names[7]],test_size=0.3,random_state=42)
tr_predict = clf.predict(X_test)
print(clf.score(X_test,y_test))

print(classification_report(y_test,tr_predict,target_names=target))

from sklearn import tree

import pydotplus
dot_data = tree.export_graphviz(clf, out_file=None,feature_names=names[0:6],class_names=target,filled=True, rounded=True,special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("E:/zheda/project/disease/infection/disease0.pdf")

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier(criterion='entropy',max_depth=6,min_samples_split=8)
dtree.fit(X_trian,y_train)

tr_predict = dtree.predict(X_test)
print(dtree.score(X_test,y_test))
print(classification_report(y_test,tr_predict,target_names=target))



from sklearn import tree
target = ['0','1']
import pydotplus
dot_data = tree.export_graphviz(dtree, out_file=None,feature_names=names[0:6],class_names=target,filled=True, rounded=True,special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("E:/zheda/project/disease/infection/disease.pdf")

import pydotplus
from IPython.display import Image
dot_data = tree.export_graphviz(dtree, out_file=None,feature_names=names[0:6],class_names=target,filled=True, rounded=True,special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())

from sklearn.datasets import load_iris
iris = load_iris()
