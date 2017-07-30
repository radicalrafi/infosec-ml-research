from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score,accuracy_score,confusion_matrix
from sklearn.externals import joblib
import pandas as pd

import pickle

Dataset = pd.read_csv('dataset20.csv')

y = Dataset['clean']
X = Dataset.drop('clean',axis = 1)


X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.2,random_state=0)


clf = RandomForestClassifier(n_estimators = 100)
clf.fit(X_train,Y_train)
y_pred = clf.predict(X_test)





print accuracy_score(Y_test,y_pred,normalize = True)
print roc_auc_score(Y_test,y_pred)
tn, fp, fn, tp = confusion_matrix(Y_test,y_pred).ravel()

print "True Positive = ",tp
print "False Positive = ",fp
print "True Negative = ",tn
print "False Negative= ",fn
joblib.dump(clf,'classifier.pkl')

