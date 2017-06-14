# ds.py

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 11:32:25 2017

@author: ADASNURK
"""

def decision_tree():
    from base import base_found
    from sklearn import tree
    
    X, X_test, y = base_found()

    ds = tree.DecisionTreeClassifier()
    ds.fit(X, y)
    acc_ds = round(ds.score(X, y) * 100, 2)
    acc_ds
    print 'Decision Tree Classifier Accuracy: {}'.format(acc_ds)
    return acc_ds

decision_tree()