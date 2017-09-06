# logreg.py

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 10:56:50 2017

@author: ADASNURK
"""

def logreg():
    from base import base_found
    from sklearn import linear_model
    
    X, X_test, y = base_found()

    logreg = linear_model.LogisticRegression()
    logreg.fit(X, y)
    acc_log = round(logreg.score(X, y) * 100, 2)
    acc_log
    print 'Logisitic Regression Accuracy: {}'.format(acc_log)
    return acc_log