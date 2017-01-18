"""
    learn TfidfVectorizer / TfidfTransformer
    TfidfVectorizer:
        Convert a collection of raw documents to a matrix of TF-IDF features.
    TfidfTransformer:
        Transform a count matrix to a normalized tf or tf-idf representation
"""
from sklearn.feature_extraction.text import TfidfTransformer

transformer = TfidfTransformer(smooth_idf=False)
counts = [
    [3, 0, 1],
    [2, 0, 0],
    [3, 0, 0],
    [4, 0, 0],
    [3, 2, 0],
    [3, 0, 2]
    ]
tfidf = transformer.fit_transform(counts)

print transformer.idf_
# [ 1.          2.79175947  2.09861229]
print(tfidf.toarray())
# [[ 0.81940995  0.          0.57320793]
#  [ 1.          0.          0.        ]
#  [ 1.          0.          0.        ]
#  [ 1.          0.          0.        ]
#  [ 0.47330339  0.88089948  0.        ]
#  [ 0.58149261  0.          0.81355169]]



transformer = TfidfTransformer(smooth_idf=True)
tfidf = transformer.fit_transform(counts)

print transformer.idf_
# [ 1.          2.25276297  1.84729786]
print(tfidf.toarray())
# [[ 0.85151335  0.          0.52433293]
#  [ 1.          0.          0.        ]
#  [ 1.          0.          0.        ]
#  [ 1.          0.          0.        ]
#  [ 0.55422893  0.83236428  0.        ]
#  [ 0.63035731  0.          0.77630514]]




