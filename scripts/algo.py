# Store user selected algorithms

# Error Handling - General
# User does not send any selection - default selection (Minimum 1)


import pandas as pd
import sys
import json



def falgo(ialgo_list=None):

    # Algorithm selection will come from Node

    with open('config.json') as input_file:
        data = json.load(input_file)

    ialgo_list = list(data['algo'])

    oalgo_list = pd.Series(ialgo_list).values
    return oalgo_list


# Uncomment the following for Node

# ialgo_list = sys.argv[1:]
# oalgo_list = falgo(ialgo_list)
# print oalgo_list
# sys.stdout.flush()
