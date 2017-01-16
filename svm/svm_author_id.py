#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

from sklearn import svm
from sklearn.metrics import accuracy_score

# clf = svm.SVC(kernel='linear')
# clf = svm.SVC(kernel='rbf')
# clf = svm.SVC(C=10.0, kernel='rbf')
# clf = svm.SVC(C=100.0, kernel='rbf')
# clf = svm.SVC(C=1000.0, kernel='rbf')
clf = svm.SVC(C=10000.0, kernel='rbf')

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

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

print('Result: {}, {}, {}'.format(pred[10], pred[26], pred[50]))
# 1,0,1

sum = 0
for p in pred:
    sum = sum + p
print('Sum: {}'.format(sum))
# Sum: 877

# 100% samples, linear:
# no. of Chris training emails: 7936
# no. of Sara training emails: 7884
# training time:198.603 s.
# predicting time:21.038 s.
# The test accuracy is: 0.984072810011

# 1% samples, linear:
# training time:0.126 s.
# predicting time:1.236 s.
# The test accuracy is: 0.884527872582

# 1% samples, rbf(Radial Basis Function):
# training time:0.143 s.
# predicting time:1.367 s.
# The test accuracy is: 0.616040955631

# 1% samples, rbf(Radial Basis Function), C=10.0:
# training time:0.151 s.
# predicting time:1.363 s.
# The test accuracy is: 0.616040955631

# 1% samples, rbf(Radial Basis Function), C=100.0:
# training time:0.132 s.
# predicting time:1.327 s.
# The test accuracy is: 0.616040955631

# 1% samples, rbf(Radial Basis Function), C=1000.0:
# training time:0.129 s.
# predicting time:1.313 s.
# The test accuracy is: 0.821387940842

# 1% samples, rbf(Radial Basis Function), C=10000.0:
# training time:0.125 s.
# predicting time:1.081 s.
# The test accuracy is: 0.892491467577

# 100% samples, rbf(Radial Basis Function), C=10000.0:
#  training time:129.331 s.
# predicting time:13.476 s.
# The test accuracy is: 0.990898748578
#########################################################


