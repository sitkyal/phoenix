# Predictor Selector

# 1. Get Label
# 2. Determine Lable Type
# 3. If Label = Continous, then send:
#    Regression Metrics and Algorithms to Display
#    else send Classification Metrics and Algorithms to Display
# 4. Pass the predictor type flag


from label_features import flabel_features

ilabel, ifeatures = flabel_features()
from load import fload_csv

fname = 'train.csv'
df, size = fload_csv(fname)

import json

for c in ilabel:
    if (df[c].unique().size*1.0 / df[c].count()) > 0.20:
        predictor_flag = 'R'
        algo_json = {"algo": ["Linear_Regression", "Lasso", "Ridge"]}
        with open('algo.json', 'w') as outfile:
            json.dump(algo_json, outfile)

        print str(c) + " Continous"
        print algo_json
    else:
        predictor_flag = 'C'
        print str(c) + " Discrete"
        algo_json = {"algo": ["decision_tree",
        "Random_Forest_Classifier",
        "knn",
        "AdaBoost_Classifier",
        "GradientBoosting_Classifier",
        "Logistic_Regression",
        "svm",
        "XGBoost_Classifier"]}
        with open('algo.json', 'w') as outfile:
            json.dump(algo_json, outfile)

