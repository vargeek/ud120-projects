#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features, save_key=True)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    key = point[2]
    plot.scatter(salary, bonus, color='g')
    if float(salary) >= 2.5e7 :
        print('->"{}": salary: {}, bonus: {}'.format(key, salary, bonus))
    elif float(bonus) >= 5e6 and float(salary) >= 1e6:
        print('=>"{}": salary: {}, bonus: {}'.format(key, salary, bonus))

plot.xlabel('salary')
plot.ylabel('bonus')
plot.show()
