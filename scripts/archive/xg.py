#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:43:32 2017

@author: adasnurk
"""

def xgb():
    from base import base_found
    from xgboost import XGBClassifier
    
    X, X_test, y = base_found()
       
    xgb = XGBClassifier()
    xg = xgb.fit(X, y)
    acc_xg = round(xg.score(X, y) * 100, 2)
    acc_xg
    print 'XGBoost Accuracy: {}'.format(acc_xg)
    return acc_xg


