# run_all.py

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 11:42:34 2017

@author: ADASNURK
"""

def run_all():
    import pandas as pd
    from ds import decision_tree
    from knn import knn
    from logreg import logreg
    from sv import sv
    from ensemble_methods import ensemble_methods
    from xg import xgb
    
    print('Running All')
    acc_ds = decision_tree()
    acc_knn = knn()
    acc_log = logreg()
    acc_xg = xgb()
    acc_svc = sv()
    acc_rf, acc_ab, acc_gb = ensemble_methods()
       
    # Model Performance

    models = pd.DataFrame({
    'Model': ['XGBoost','Logistic Regression', 'KNN', 'Support Vector Machines', 'Gradient Boosting',
              'Random Forest', 'Decision Tree', 'ADABoost'],
    'Score': [acc_xg, acc_log, acc_knn,acc_svc, acc_gb, acc_rf, acc_ds, acc_ab ]})
    models = models.sort_values(by='Score', ascending=True)
    print models.sort_values(by='Score', ascending=False)

run_all()