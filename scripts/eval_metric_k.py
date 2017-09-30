# Store user selected columns (label and features)

# Error Handling - General
# User does not send any selection - default selection (Max 1 for eval and default k)

import pandas as pd
import sys
import json
import logging


def fmetric_k(imetric=None, ik=None):

    emk_logger = logging.getLogger('lemk')
    try:
        emk_logger.info('Started evaluation metric and k')
        # imetric and ik will be passed in from Node
        with open('config.json') as input_file:
            data = json.load(input_file)
        imetric = str(data['evalmetric'])
        ometric = pd.Series(imetric).values
        ok = int(data['k'])
        emk_logger.info('Completed evaluation metric and k')
        return ometric, ok
    except Exception as e:
        emk_logger.exception(e)
        sys.exit(1)
        return 1

    #imetric = sys.argv[1]
    #ik = sys.argv[2:]

    #ometric, ok = fmetric_k(imetric, ik)
    #print ometric, ok
    #sys.stdout.flush()
