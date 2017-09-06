# Ensemble Methods

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 11:35:35 2017

@author: ADASNURK
"""

def ensemble_methods():
    from base import base_found
    from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
    
    X, X_test, y = base_found()

    # Random Forest
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X, y)
    acc_rf = round(rf.score(X, y) * 100, 2)
    acc_rf
    print 'Random Forest Classifier Accuracy: {}'.format(acc_rf)
    
    # ADA Boost
    
    ab = AdaBoostClassifier()
    ab.fit(X, y)
    acc_ab = round(ab.score(X, y) * 100, 2)
    acc_ab
    print 'AdaBoost Classifier Accuracy: {}'.format(acc_ab)
    
    # Gradient Boosting
    
    gb = GradientBoostingClassifier(n_estimators=200)
    gb.fit(X, y)
    acc_gb = round(gb.score(X, y) * 100, 2)
    acc_gb
    print 'Gradient Boosting Classifier Accuracy: {}'.format(acc_gb)
    
    return acc_rf, acc_ab, acc_gb