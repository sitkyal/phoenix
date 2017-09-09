# Store user selected algorithms

import pandas as pd
import sys



def falgo(ialgo_list=None):

    # Delete the following list when passing from Node

    ialgo_list=['decision_tree', 'knn', 'Random_Forest_Classifier',
          'AdaBoost_Classifier', 'GradientBoosting_Classifier', 'Logistic_Regression', 'svm', 'XGBoost_Classifier']

    oalgo_list = pd.Series(ialgo_list).values
    return oalgo_list


# Uncomment the following when passing from Node

# ialgo_list = sys.argv[1:]
# oalgo_list = falgo(ialgo_list)
# print oalgo_list
# sys.stdout.flush()
