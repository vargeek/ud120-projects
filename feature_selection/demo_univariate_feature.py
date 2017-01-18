"""
    Select features according to the k highest scores.
    should provide a Function taking two arrays X and y, 
        and returning a pair of arrays (scores, pvalues) 
        or a single array with scores.
"""

from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

iris = load_iris()
X, y = (iris.data, iris.target)

print X.shape
# (150, 4)
X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
print X_new.shape
(150, 2)

scores_pvalues = chi2(X, y)
print scores_pvalues
# ( array([  10.81782088,    3.59449902,  116.16984746,   67.24482759]), 
#   array([  4.47651499e-03,   1.65754167e-01,   5.94344354e-26, 2.50017968e-15]) )

