"""
    fetch F1 scores from result.txt
"""

import re

path = './result.txt'
file_handler = None
try:
    file_handler = open(path, 'r')
except Exception as error:
    print error
if file_handler == None:
    exit(0)

n_components = []
f1_scores = []
n_reg = re.compile(r'===================> (\d+)')
f1_reg = re.compile(r'avg \/ total(?:\s*[\d\.]+){2}(\s*[\d\.]+)(?:\s*[\d\.]+)')
for line in file_handler:
    match = n_reg.search(line)
    if match:
        n_components.append(int(match.group(1)))
    match = f1_reg.search(line)
    if match:
        f1_scores.append(float(match.group(1)))

result = zip(n_components, f1_scores)
for n, f1 in result:
    print "%d\t%f" % (n, f1)

file_handler.close()
