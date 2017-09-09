# Store user selected columns (label and features)

import pandas as pd
import sys


def flabel_features(ilabel=None, ifeatures=None):

    # ilabel and ifeatures will be passed in from Node

    ilabel = ['Survived'] # Remove once testing is done
    ifeatures = ['PassengerId','Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked', 'Cabin', 'Ticket', 'Fare'] # Remove once testing is done
    olabel = pd.Series(ilabel).values
    ofeatures = pd.Series(ifeatures).values
    return olabel, ofeatures


#ilabel = sys.argv[1]
#ifeatures = sys.argv[2:]

#olabel, ofeatures = flabel_features(ilabel, ifeatures)
#print olabel, ofeatures
#sys.stdout.flush()
