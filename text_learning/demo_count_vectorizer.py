"""
    learn CountVectorizer
"""
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)
print vectorizer
# CountVectorizer(analyzer=u'word', binary=False, decode_error=u'strict',
#         dtype=<type 'numpy.int64'>, encoding=u'utf-8', input=u'content',
#         lowercase=True, max_df=1.0, max_features=None, min_df=1,
#         ngram_range=(1, 1), preprocessor=None, stop_words=None,
#         strip_accents=None, token_pattern=u'(?u)\\b\\w\\w+\\b',
#         tokenizer=None, vocabulary=None)


corpus = [
    'This is the first document.',
     'This is the second second document.',
     'And the third one.',
     'Is this the first document?',
     ]

vectorizer.fit(corpus)
print vectorizer.get_feature_names()
# [u'and', u'document', u'first', u'is', u'one', u'second', u'the', u'third', u'this']
print vectorizer.vocabulary_.get('document')
# 1

X = vectorizer.transform(corpus)
print X.toarray()
# [[0 1 1 1 0 0 1 0 1]
#  [0 1 0 1 0 2 1 0 1]
#  [1 0 0 0 1 0 1 1 0]
#  [0 1 1 1 0 0 1 0 1]]


# vectorizer.fit(corpus)
# X = vectorizer.transform(corpus)
# =>
# X = vectorizer.fit_transform(corpus)

# The default configuration tokenizes the string by extracting words of at least 2 letters.
analyze = vectorizer.build_analyzer()
print analyze("This is a text document to analyze.")
# [u'this', u'is', u'text', u'document', u'to', u'analyze']



