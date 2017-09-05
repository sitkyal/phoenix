# Store user selected columns (label and features)

import pandas as pd
import sys


def metric_k(metric, k):

    imetric = pd.Series(metric).values
    ik = pd.Series(k).values
    return imetric, ik


metric = sys.argv[1]
k = sys.argv[2:]

# for testing
#label = pd.Series(['Survived'])
#features = pd.Series(['Pclass', 'Sex', 'Age'])

imetric, ik = metric_k(metric, k)
print imetric, ik
sys.stdout.flush()
