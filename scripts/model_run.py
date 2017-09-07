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

    cm1 = SVC()
    score1 = round(
        (cross_val_score(cm1, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 2)
    print 'KNN Score: {}'.format(score1)
    return score1


# for testing
fname = sys.argv[1]
k = 20

from pre_process import fpre_process
X, y = fpre_process(fname)
decision_tree(X, y, k)
knn(X, y, k)


#imodel = fmodel_run(imodel)
# print imodel, type(imodel)
# sys.stdout.flush()
