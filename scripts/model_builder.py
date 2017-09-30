# All Models

# Potential conflict of attributes accepted by models

from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score
import sklearn.tree
import sklearn.ensemble
import sklearn.neighbors
import sklearn.linear_model
import sklearn.svm
import xgboost
import logging
import sys

from sklearn.feature_selection import SelectFromModel

converter = {"decision_tree": sklearn.tree.DecisionTreeClassifier,
             "Random_Forest_Classifier": sklearn.ensemble.RandomForestClassifier,
             "knn": sklearn.neighbors.KNeighborsClassifier,
             "AdaBoost_Classifier": sklearn.ensemble.AdaBoostClassifier,
             "GradientBoosting_Classifier": sklearn.ensemble.GradientBoostingClassifier,
             "Logistic_Regression": sklearn.linear_model.LogisticRegression,
             "svm": sklearn.svm.SVC,
             "XGBoost_Classifier": xgboost.XGBClassifier}

def model_builder(mname, X, y, k, eval_metric=None):

    mbuilder_logger = logging.getLogger('lmbuilder')

    try:
        mbuilder_logger.info('Start cross validation, fitting and scoring for %s' %mname)
        model_name = converter[mname]
        if mname == 'svm':
            cm = model_name(probability=True)
            ypred = cross_val_predict(cm, X,y, cv=k, n_jobs=-1)
            y_score = cross_val_predict(cm, X, y, cv=k, n_jobs=-1, method='predict_proba')
        else:
            cm = model_name()
            ypred = cross_val_predict(cm, X,y, cv=k, n_jobs=-1)
            y_score = cross_val_predict(cm, X, y, cv=k, n_jobs=-1, method='predict_proba')
        #score = round(
         #   (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
        score = accuracy_score(y, ypred)
        model_name = mname
        print mname + ' {}'.format(score)
        mbuilder_logger.info('Complete cross validation, fitting and scoring for %s' %mname)
        return model_name, score, y, ypred, y_score
    except Exception as e:
        mbuilder_logger.exception(e)
        sys.exit(1)
        return 1
