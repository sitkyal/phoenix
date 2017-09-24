# Store user selected columns (label and features)

# Error Handling - General
# User does not send any selection - default selection (Minimum 1 for label and feature)

import pandas as pd
import sys
import json


def flabel_features(ilabel=None, ifeatures=None):

    # ilabel and ifeatures will be passed in from Node

    with open('config.json') as input_file:
        data = json.load(input_file)

    ilabel = str(data['label'])
    ifeatures = list(data['features'])

    olabel = pd.Series(ilabel).values
    ofeatures = pd.Series(ifeatures).values
    return olabel, ofeatures


#ilabel = sys.argv[1]
#ifeatures = sys.argv[2:]

#olabel, ofeatures = flabel_features(ilabel, ifeatures)
#print olabel, ofeatures
#sys.stdout.flush()
