# Store user selected columns (label and features)

import pandas as pd
import sys


def fmetric_k(imetric=None, ik=None):

    # imetric and ik will be passed in from Node

    #ometric = 'accuracy' # Remove once testing is done
    ok = 25 # Remove once testing is done
    ometric = pd.Series(imetric).values
    #ok = pd.Series(ok).values
    return ometric, ok

#imetric = sys.argv[1]
#ik = sys.argv[2:]

# for testing
#label = pd.Series(['Survived'])
#features = pd.Series(['Pclass', 'Sex', 'Age'])

#ometric, ok = fmetric_k(imetric, ik)
#print ometric, ok
#sys.stdout.flush()
