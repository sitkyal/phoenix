# Store user selected columns (label and features)

import pandas as pd
import sys


def flabel_features(ilabel, ifeatures):

    olabel = pd.Series(ilabel).values
    oeatures = pd.Series(ifeatures).values
    return olabel, ofeatures


ilabel = sys.argv[1]
ifeatures = sys.argv[2:]

# for testing
#label = pd.Series(['Survived'])
#features = pd.Series(['Pclass', 'Sex', 'Age'])

olabel, ofeatures = flabel_features(ilabel, ifeatures)
print olabel, ofeatures
sys.stdout.flush()
