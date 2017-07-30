import analyzer
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score,accuracy_score

dataset = pd.read_csv("malware-dataset.csv")

X = dataset.drop('clean',axis = 1)
y = dataset['clean']

X = np.asarray(X)
y = np.asarray(y)
X = X[:,1:]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state=43)

clf = RandomForestClassifier(n_estimators=10, random_state=33)
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

print accuracy_score(y_test,y_pred)

print len(y_pred)

good = 0
bad = 0
for i in range(0,len(y_pred)):
    if y_pred[i] == y_test[i]:
        good += 1
    else:
        bad += 1

print good
print bad