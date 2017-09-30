# Store user selected columns (label and features)

# Error Handling - General
# User does not send any selection - default selection (Minimum 1 for label and feature)

import pandas as pd
import sys
import json
import logging


def flabel_features(ilabel=None, ifeatures=None):

    label_feature_logger = logging.getLogger('llabelfeature')

    # ilabel and ifeatures will be passed in from Node
    try:
        label_feature_logger.info('Started features and label extraction')

        with open('config.json') as input_file:
            data = json.load(input_file)

        ilabel = str(data['label'])
        ifeatures = list(data['features'])

        olabel = pd.Series(ilabel).values
        ofeatures = pd.Series(ifeatures).values
        label_feature_logger.info('Completed Features and label extraction')
        return olabel, ofeatures

    except Exception as e:
        label_feature_logger.exception(e)
        return 1
        sys.exit(1)


#ilabel = sys.argv[1]
#ifeatures = sys.argv[2:]

#olabel, ofeatures = flabel_features(ilabel, ifeatures)
#print olabel, ofeatures
#sys.stdout.flush()
