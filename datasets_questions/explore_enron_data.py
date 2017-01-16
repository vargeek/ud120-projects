#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

# laod data
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print('There are {} persons'.format(len(enron_data)))
# There are 146 persons

features_number = len(enron_data[enron_data.keys()[0]])
print('Each person has {} features'.format(features_number))
# Each person has 21 features

poi_sum = 0
for key in enron_data.keys():
    person = enron_data[key]
    # print(key)
    if person['poi']:
        poi_sum += 1

print('Person of interest: {}'.format(poi_sum))
# Person of interest: 18

print('total_stock_value of James Prentice: {}'.format(enron_data['PRENTICE JAMES']['total_stock_value']))
# total_stock_value of James Prentice: 1095040

print('from_this_person_to_poi of Wesley Colwell: {}'.format(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))
# from_this_person_to_poi of Wesley Colwell: 698242

print('exercised_stock_options of Jeffrey Skilling: {}'.format(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))

print('total_payments of LAY KENNETH L: {}'.format(enron_data['LAY KENNETH L']['total_payments']))
# chairman
# total_payments of LAY KENNETH L: 103559793

print('total_payments of FASTOW ANDREW S: {}'.format(enron_data['FASTOW ANDREW S']['total_payments']))
# CFO
# total_payments of FASTOW ANDREW S: 2424083

print('total_payments of SKILLING JEFFREY K: {}'.format(enron_data['SKILLING JEFFREY K']['total_payments']))
# CEO
# total_payments of SKILLING JEFFREY K: 8682716
