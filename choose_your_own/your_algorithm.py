#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from time import time
from sklearn.ensemble import AdaBoostClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary





accuracy_max = -10^8
for n in [1,3,10,30,100,300,1000,3000]:
    clf_temp = clf_temp = RandomForestClassifier(n_estimators=n)
    clf_temp.fit(features_train, labels_train)
    pred = clf_temp.predict(features_test)
    accuracy = accuracy_score(pred, labels_test)
    print('The test accuracy of {} is: {}'.format(n, accuracy))
    if accuracy > accuracy_max:
        accuracy_max = accuracy
        clf = clf_temp



try:
    prettyPicture(clf_temp, features_test, labels_test)
except NameError:
    pass
