# Store user selected columns (label and features)

import pandas as pd
import sys
import json


def fmetric_k(imetric=None, ik=None):

    # imetric and ik will be passed in from Node

    with open('config.json') as input_file:
        data = json.load(input_file)


    imetric = str(data['evalmetric'])

    ometric = pd.Series(imetric).values
    ok = int(data['k'])
    return ometric, ok

#imetric = sys.argv[1]
#ik = sys.argv[2:]

#ometric, ok = fmetric_k(imetric, ik)
#print ometric, ok
#sys.stdout.flush()
