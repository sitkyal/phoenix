# Store user selected algorithms

# Error Handling - General
# User does not send any selection - default selection (Minimum 1)


import pandas as pd
import sys
import json
import logging



def falgo(ialgo_list=None):

    algo_logger = logging.getLogger('lalgo')

    # Algorithm selection will come from Node
    try:
        algo_logger.info('Started model selection')
        with open('config.json') as input_file:
            data = json.load(input_file)
        ialgo_list = list(data['algo'])
        oalgo_list = pd.Series(ialgo_list).values
        algo_logger.info('Completed model selection')
        return oalgo_list
    except Exception as e:
        algo_logger.exception(e)
        sys.exit(1)
        return 1


# Uncomment the following for Node

# ialgo_list = sys.argv[1:]
# oalgo_list = falgo(ialgo_list)
# print oalgo_list
# sys.stdout.flush()
