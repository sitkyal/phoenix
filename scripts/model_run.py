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
import json
warnings.filterwarnings("ignore", category=DeprecationWarning)
from evaluation import rocc, conf_mat

# wrap model_run in a function in order to send data to evaluation

with open('config.json') as input_file:
    data = json.load(input_file)

fname = str(data['filename'])

# Get X, y

print "Preprocessing Started....."

from pre_process import fpre_process
X, y = fpre_process(fname)

print "Preprocessing Complete...."

# Get the Models to run


from algo import falgo
imodel = falgo()


# Get Evaluation Metric and k

from eval_metric_k import fmetric_k
ometric, k = fmetric_k()

cmatrix_json = {}
roc_json = {}
print "Modeling Started...."


for i in tqdm(imodel):
    from model_builder import model_builder
    model_name, score, ypred, y = model_builder(i, X, y, k)

    # calculate evaluation components

    # Confusion Matrix

    cmatrix = conf_mat(y, ypred)
    cmatrix_json.update({model_name: cmatrix.tolist()})


    # ROC Curve and AUC

    fpr, tpr = rocc(y, ypred)
    roc_param = [fpr, tpr]
    roc_json.update({model_name:{"fpr": fpr.tolist(), "tpr": tpr.tolist()}})

    # Feature Importance


    # convert into function name
    #algo_func = converter[i]
    #algo_func(X, y, k)

with open('conf.json', 'w') as outfile:
        json.dump(cmatrix_json, outfile)

with open('roc.json', 'w') as outfile:
        json.dump(roc_json, outfile)

print "Modeling Complete"
