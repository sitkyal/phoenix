# sv.py

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 11:25:21 2017

@author: ADASNURK
"""

def sv():
    from base import base_found
    from sklearn.svm import SVC
    
    X, X_test, y = base_found()

    sv = SVC()
    sv.fit(X, y)
    acc_sv = round(sv.score(X, y) * 100, 2)
    acc_sv
    print 'Support Vector Machine Accuracy: {}'.format(acc_sv)
    return acc_sv
