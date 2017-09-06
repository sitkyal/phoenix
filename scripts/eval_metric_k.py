# Store user selected columns (label and features)

import pandas as pd
import sys


def fmetric_k(imetric, ik):

    ometric = pd.Series(ometric).values
    ok = pd.Series(ok).values
    return ometric, ok


imetric = sys.argv[1]
ik = sys.argv[2:]

# for testing
#label = pd.Series(['Survived'])
#features = pd.Series(['Pclass', 'Sex', 'Age'])

ometric, ok = metric_k(imetric, ik)
print ometric, ok
sys.stdout.flush()
