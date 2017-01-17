#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    ### your code goes here
    # print(len(predictions), len(predictions[0]))
    # print(len(ages), len(ages[0]))
    # print(len(net_worths), len(net_worths[0]))

    for index in range(len(predictions)):
        age = ages[index][0]
        pred = predictions[index][0]
        net_worth = net_worths[index][0]
        error = (pred - net_worth) ** 2
        cleaned_data.append((age, net_worth, error))
    cleaned_data.sort(key=lambda t: t[2])
    cleaned_data = cleaned_data[0:int(len(cleaned_data) * 0.9)]
    return cleaned_data

