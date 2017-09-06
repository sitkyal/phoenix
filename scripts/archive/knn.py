   # knn.py

    # -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 11:23:02 2017

@author: ADASNURK
"""

def knn():
    from base import base_found
    from sklearn import neighbors
    
    X, X_test, y = base_found()

    knn = neighbors.KNeighborsClassifier(n_neighbors=5)
    knn.fit(X, y)
    acc_knn = round(knn.score(X, y) * 100, 2)
    acc_knn
    print 'KNN Accuracy: {}'.format(acc_knn)
    return acc_knn