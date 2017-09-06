# Get Model Input and Run Models

# Get X, y, k and evaluation metrics
# Get selected models
# Run each model function
# Return Model and Score


import pandas as pd
import sys


# def fmodel_run(imodel):

#imodel = list(pd.Series(imodel).values)

# for i in imodel:
#    imodel, score = i()
#    return imodel, score


def decision_tree(k, eval_metric=None):
    from sklearn import tree
    from sklearn.model_selection import cross_val_score

    from base import base_found
    X, X_test, y = base_found()

    # Model

    cm = tree.DecisionTreeClassifier()
    score = round((cross_val_score(cm, X, y, cv=k,
                                   scoring=eval_metric, n_jobs=-1).max()), 2)
    print 'Decision Tree Classifier Score: {}'.format(score)
    return score


def knn(k, eval_metric=None):
    #from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import cross_val_score

    from base import base_found
    X, X_test, y = base_found()

    cm1 = SVC()
    score1 = round(
        (cross_val_score(cm1, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 2)
    print 'KNN Score: {}'.format(score1)
    return score1

# for testing


decision_tree(20)
knn(20)

#imodel = sys.argv[1:]

#imodel = fmodel_run(imodel)
# print imodel, type(imodel)
# sys.stdout.flush()
