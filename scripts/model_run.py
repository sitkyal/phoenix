# Get Model Input and Run Models

# Get X, y, k and evaluation metrics
# Get selected models
# Run each model function
# Return Model and Score


import pandas as pd
import sys
#import models
import warnings
import json
import numpy as np
import logging
import logging.config
from evaluation import rocc, conf_mat, prc
from tqdm import tqdm

warnings.filterwarnings("ignore", category=DeprecationWarning)


# set up logging

logging.config.fileConfig('mwlog_conf', disable_existing_loggers=False)
logger = logging.getLogger("mwApp")

# wrap model_run in a function in order to send data to evaluation
logger.info('START')

with open('config.json') as input_file:
    data = json.load(input_file)

fname = str(data['filename'])

# Get X, y

from pre_process import fpre_process
X, y = fpre_process(fname)

# Get the Models to run

from algo import falgo
imodel = falgo()


# Get Evaluation Metric and k

from eval_metric_k import fmetric_k
ometric, k = fmetric_k()

# initialize variables for Classification

cmatrix_json = {}
cm_eval_metrics_json = {}
roc_json = {}
prc_json = {}
roc_list = []
prc_list = []
cmatrix_list = []
roc_array = np.zeros(shape=(3, 3))
prc_array = np.zeros(shape=(3, 3))
cm_eval_metrics = []

# initiate variables for Regression

logger.info("Modeling Started....")


for i in tqdm(imodel):
    from model_builder import model_builder
    model_name, score, y, ypred, y_score = model_builder(i, X, y, k)

    # Get evaluation components

    # Confusion Matrix

    cmatrix, TP, TN, FP, FN, Specificity, Sensitivity, Accuracy, Error_Rate, Precision, FPR, f1score, neglogloss, mcc = conf_mat(
        y, ypred)

    # prepare data for output formats

    cmatrix_list.append([model_name, TP, TN, FP, FN])
    cmatrix_json.update({model_name: cmatrix.tolist()})
    cm_eval_metrics.append([model_name, Specificity, Sensitivity,
                            Accuracy, Error_Rate, Precision, FPR, f1score, neglogloss, mcc])
    cm_eval_metrics_json.update({model_name: cm_eval_metrics})

    # ROC Curve and AUC
    fpr, tpr, auc_score = rocc(y, y_score)

    # prepare data for output formats

    m_list = []
    roc_list = []
    m_list = [model_name for i in fpr]
    roc_list.append(m_list)
    roc_list.append(fpr)
    roc_list.append(tpr)
    roc_list_t = np.array(roc_list).T
    roc_array = np.append(roc_array, roc_list_t, axis=0)
    roc_json.update({model_name: {"fpr": fpr.tolist(), "tpr": tpr.tolist()}})

    # Precision Recall Curve
    precision, recall = prc(y, y_score)

    # prepare data for output formats

    m_list1 = []
    prc_list = []
    m_list1 = [model_name for i in precision]
    prc_list.append(m_list1)
    prc_list.append(precision)
    prc_list.append(precision)
    prc_list_t = np.array(prc_list).T
    prc_array = np.append(prc_array, prc_list_t, axis=0)
    prc_json.update({model_name: {"precision": precision.tolist(),
                    "recall": recall.tolist()}})

logger.info("Modeling Complete")

logger.info('Outputting to CSV')
# Output files
# CSV

cmatrix_csv = pd.DataFrame(data=cmatrix_list, columns=[
                           'Model', 'TP', 'TN', 'FP', 'FN'])
cmatrix_csv.to_csv('output/cmatrix.csv', index=False)
cm_eval_metrics_csv = pd.DataFrame(data=cm_eval_metrics, columns=[
                                   'Model', 'Specificity', 'Sensitivity',
                                   'Accuracy', 'Error Rate', 'Precision',
                                   'FPR', 'f1 Score', 'NegLogLoss', 'MCC'])
cm_eval_metrics_csv.to_csv('output/cm_eval_metrics.csv', index=False)

roc_array = np.delete(roc_array, (0, 1, 2), axis=0)
roc_csv = pd.DataFrame(data=roc_array, columns=['Model', 'FPR', 'TPR'])
roc_csv.to_csv('output/roc.csv', index=False)


prc_array = np.delete(prc_array, (0, 1, 2), axis=0)
prc_csv = pd.DataFrame(data=prc_array, columns=['Model', 'Precision', 'Recall'])
prc_csv.to_csv('output/prc.csv', index=False)

# JSON
logger.info('Outputting to JSON')

with open('output/conf.json', 'w') as outfile:
    json.dump(cmatrix_json, outfile)

with open('output/cm_eval_metrics.json', 'w') as outfile:
    json.dump(cm_eval_metrics_json, outfile)

with open('output/roc.json', 'w') as outfile:
    json.dump(roc_json, outfile)

with open('output/prc.json', 'w') as outfile:
    json.dump(prc_json, outfile)

logger.info('Model Publication Complete')
logger.info('END')
