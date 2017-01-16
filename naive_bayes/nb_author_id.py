#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clr = GaussianNB()

start_time = time()
clr.fit(features_train, labels_train)
end_time = time()
print("training time:{} s.".format(round(end_time - start_time, 3)))

start_time = time()
pred = clr.predict(features_test)
end_time = time()
print("predicting time:{} s.".format(round(end_time - start_time, 3)))

# accuracy = clr.score(features_test, labels_test)
accuracy = accuracy_score(pred, labels_test)
print("The test accuracy is: {}".format(accuracy))

# no. of Chris training emails: 7936
# no. of Sara training emails: 7884
# training time:3.001 s.
# predicting time:0.224 s.
# The test accuracy is: 0.973265073948

#########################################################


