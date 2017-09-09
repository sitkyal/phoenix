# Get Model Input and Run Models

# Get X, y, k and evaluation metrics
# Get selected models
# Run each model function
# Return Model and Score


import pandas as pd
import sys
import models


def decision_tree(X, y, k, eval_metric=None):
    from sklearn import tree
    from sklearn.model_selection import cross_val_score

    # Model

    cm = tree.DecisionTreeClassifier()
    score = round((cross_val_score(cm, X, y, cv=k,
                                   scoring=eval_metric, n_jobs=-1).max()), 2)
    print 'Decision Tree Classifier Score: {}'.format(score)
    return score


def knn(X, y, k, eval_metric=None):
    #from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import cross_val_score

    cm = SVC()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 2)
    print 'KNN Score: {}'.format(score)
    return score


# for testing
fname = sys.argv[1]
imodel = ['decision_tree', 'knn']
converter = {"decision_tree": decision_tree, "knn": knn}
k = 20

from pre_process import fpre_process
X, y = fpre_process(fname)
#decision_tree(X, y, k)
#knn(X, y, k)


for i in imodel:

    # convert into function name
    algo_func = converter[i]
    algo_func(X,y,k)

