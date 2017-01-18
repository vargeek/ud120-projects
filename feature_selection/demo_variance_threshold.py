"""
    we want to remove all features that are either one or zero (on or off)
        in more than 80% of the samples.
    Boolean features are Bernoulli random variables
    var(x) = p(x)*(1-p(x))
"""
from sklearn.feature_selection import VarianceThreshold
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel = VarianceThreshold(threshold=(0.8 * (1 - 0.8)))
X_new = sel.fit_transform(X)
print sel.variances_
# [ 0.13888889  0.22222222  0.25      ]
print X_new.shape
# (6, 2)
