# Get Model Input and Run Models

# Get X, y, k and evaluation metrics
# Get selected models
# Run each model function
# Return Model and Score


import pandas as pd
import sys
import models
import warnings
from tqdm import tqdm
warnings.filterwarnings("ignore", category=DeprecationWarning)


# for testing
fname = sys.argv[1]

# Get X, y

from pre_process import fpre_process
X, y = fpre_process(fname)

# Get the Models to run

from algo import falgo
imodel = falgo()


# Get Evaluation Metric and k

from eval_metric_k import fmetric_k
ometric, k = fmetric_k()


# Convert to functions

converter = {"decision_tree": models.decision_tree, "knn": models.knn,
             "Random_Forest_Classifier": models.Random_Forest_Classifier,
             "AdaBoost_Classifier": models.AdaBoost_Classifier,
             "GradientBoosting_Classifier": models.GradientBoosting_Classifier,
             "Logistic_Regression": models.Logistic_Regression, "svm": models.svm, "XGBoost_Classifier": models.XGBoost_Classifier}


# imodel = ['decision_tree', 'knn', 'Random_Forest_Classifier',
#          'AdaBoost_Classifier', 'GradientBoosting_Classifier', 'Logistic_Regression', 'svm', 'XGBoost_Classifier']


for i in tqdm(imodel):

    # convert into function name
    algo_func = converter[i]
    algo_func(X, y, k)
