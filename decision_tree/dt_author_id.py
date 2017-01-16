#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# no. of Chris training emails: 7936
# no. of Sara training emails: 7884

# print('dimension of features: {}'.format(len(features_train[0])))
# dimension of features: 3785
# selector = SelectPercentile(f_classif, percentile=1)
# dimension of features: 379

from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier(min_samples_split=40)
begin_time = time()
clf.fit(features_train, labels_train)
end_time = time()
print("training time:{} s.".format(round(end_time - begin_time, 3)))

begin_time = time()
pred = clf.predict(features_test)
end_time = time()
print("predicting time:{} s.".format(round(end_time - begin_time, 3)))

accuracy = accuracy_score(pred, labels_test)
print('The test accuracy is: {}'.format(accuracy))

# percentile=10
# training time:62.406 s.
# predicting time:0.08 s.
# The test accuracy is: 0.978953356086

# percentile=1
# training time:5.358 s.
# predicting time:0.005 s.
# The test accuracy is: 0.966439135381


#########################################################


