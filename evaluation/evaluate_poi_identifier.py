#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score

clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)

pred = clf.predict(features)
accuracy = accuracy_score(labels, pred)
print 'overfitting accuracy: %f' % accuracy




features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
accuracy = accuracy_score(labels_test, pred)
print 'test accuracy: %f' % accuracy

print 'There are %d people in the test set' % len(labels_test)

sum_poi_test = len([label for label in labels_test if label > 0.9])
print 'There are %d poi in the test set' % sum_poi_test


true_pos = len([(p,ac) for (p,ac) in zip(pred, labels_test) if p == 1 and ac == 1])
print 'there are %d true positives' % true_pos
precision = precision_score(labels_test, pred)
print 'precision %f' % precision
recall = recall_score(labels_test, pred)
print 'recall %f' % recall

