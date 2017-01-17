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

# chairman: LAY KENNETH L
# CFO: FASTOW ANDREW S
# CEO: SKILLING JEFFREY K
# POIs: 35

names = enron_data.keys()
person_count = len(names)
features_number = len(enron_data[names[0]])

poi_count = 0
valid_salary_count = 0
valid_email_count = 0
nan_payment_count = 0
poi_nan_payment_count = 0

for name in names:
    person = enron_data[name]
    if person['poi']:
        poi_count += 1
    if person['salary'] != 'NaN':
        valid_salary_count += 1
    if person['email_address'] != 'NaN':
        valid_email_count += 1
    if person['total_payments'] == 'NaN':
        nan_payment_count += 1
        if person['poi']:
            poi_nan_payment_count += 1

invalid_payment_pct = float(nan_payment_count) / person_count
poi_invalid_payment_pct = float(poi_nan_payment_count) / poi_count

print('There are {} persons'.format(person_count))
print('Each person has {} features'.format(features_number))
print('Person of interest: {}'.format(poi_count))
print('valid salary: {}'.format(valid_salary_count))
print('valid email: {}'.format(valid_email_count))
print('nan payment: {}, pct: {}'.format(nan_payment_count, round(invalid_payment_pct,3)))
print('nan payment of poi: {}, pct: {}'.format(poi_nan_payment_count, round(poi_invalid_payment_pct, 3)))

# There are 146 persons
# Each person has 21 features
# Person of interest: 18
# valid salary: 95
# valid email: 111
# nan payment: 21, pct: 0.144
# nan payment of poi: 0, pct: 0.0


print('=================')

print('total_stock_value of James Prentice: {}'.format(enron_data['PRENTICE JAMES']['total_stock_value']))
# total_stock_value of James Prentice: 1095040

print('from_this_person_to_poi of Wesley Colwell: {}'.format(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))
# from_this_person_to_poi of Wesley Colwell: 698242

print('exercised_stock_options of Jeffrey Skilling: {}'.format(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))

print('total_payments of LAY KENNETH L: {}'.format(enron_data['LAY KENNETH L']['total_payments']))

print('total_payments of FASTOW ANDREW S: {}'.format(enron_data['FASTOW ANDREW S']['total_payments']))

print('total_payments of SKILLING JEFFREY K: {}'.format(enron_data['SKILLING JEFFREY K']['total_payments']))


# total_stock_value of James Prentice: 1095040
# from_this_person_to_poi of Wesley Colwell: 11
# exercised_stock_options of Jeffrey Skilling: 19250000
# total_payments of LAY KENNETH L: 103559793
# total_payments of FASTOW ANDREW S: 2424083
# total_payments of SKILLING JEFFREY K: 8682716