# Base 

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 10:41:41 2017

@author: ADASNURK
"""

# import libraries and preprocess

def base_found():
    import pandas as pd
    import numpy as np
     
    # import data files
    df = pd.read_csv('train.csv')
    df_test = pd.read_csv('test.csv')
    combine = [df, df_test]
    
    # Encode for Sex and Embarked 
    
    for col in combine:
        col.Sex.replace('male', 0, inplace=True)
        col.Sex.replace('female', 1, inplace=True)
        
    # Feature Engineering
    
    # Travelling with family may include your chances of survival. 
    
    for col in combine:
        col['IsAlone'] = 0
        col['Family'] = col['Parch'] + col['SibSp'] + 1
        col.loc[col['Family'] == 1, 'IsAlone'] = 1
    
    # Age and Embarked have null values and will need to be replaced
    
    #df.Age.replace(np.NaN, df.Age.mean(), inplace=True)
    for col in combine:
        col.Embarked.replace(np.NaN, 'S', inplace=True)
        col.Fare.replace(np.NaN, col.Fare.median(), inplace=True)
        
    # Encode for Sex and Embarked on Test
    
    for col in combine:
        col.Embarked.replace('C', 1, inplace=True)
        col.Embarked.replace('Q', 2, inplace=True)
        col.Embarked.replace('S', 3, inplace=True)
        col.Embarked = col.Embarked.astype(np.int)
        
    # Dropping Cabin due to too many Nulls and Tickets that don't have any specific value.
    # Name may be interesting but not now. 
    
    for col in combine:
        col.drop(['Ticket', 'Cabin'], axis=1, inplace=True)
        
    for col in combine:
        col.Age.replace(np.NaN, col.Age.mean(), inplace=True)
        
    # Create Age Bands
    
    for col in combine:
        col.loc[ col['Age'] <= 16, 'Age'] = 0
        col.loc[(col['Age'] > 16) & (col['Age'] <= 32), 'Age'] = 1
        col.loc[(col['Age'] > 32) & (col['Age'] <= 48), 'Age'] = 2
        col.loc[(col['Age'] > 48) & (col['Age'] <= 64), 'Age'] = 3
        col.loc[ col['Age'] > 64, 'Age']
    
    # So what's in the name? 
    
    for col in combine:
        col['Title'] = col.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    
        
    # Replace all Titles with low frequencies as 'Rare'
    
    for col in combine:
        col['Title'] = col['Title'].replace(['Dr', 'Rev','Col', 'Major', 'Countess', 'Lady', 'Jonkheer', 'Don', 'Capt', 'Sir', 'Dona'], 'Rare')
        
        col['Title'] = col['Title'].replace('Mlle', 'Miss')
        col['Title'] = col['Title'].replace('Ms', 'Miss')
        col['Title'] = col['Title'].replace('Mme', 'Mrs')
        
    # Encode
    
    for col in combine:
        col.Title.replace('Mr', 1, inplace=True)
        col.Title.replace('Mrs', 3, inplace=True)
        col.Title.replace('Miss', 2, inplace=True)
        col.Title.replace('Master', 4, inplace=True)
        col.Title.replace('Rare', 5, inplace=True)
        
    for dataset in combine:
        dataset.loc[ dataset['Fare'] <= 7.91, 'Fare'] = 0
        dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare'] = 1
        dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare']   = 2
        dataset.loc[ dataset['Fare'] > 31, 'Fare'] = 3
        dataset['Fare'] = dataset['Fare'].astype(int)
    
    for dataset in combine:
        dataset['Age*Class'] = dataset.Age * dataset.Pclass
    
    columns = ['Pclass', 'Sex', 'Age', 'IsAlone','Fare', 'Title', 'Embarked', 'Age*Class']
    
    X = df[columns].as_matrix().astype(np.float)
    X_test = df_test[columns].as_matrix().astype(np.float)
    y = df['Survived'].as_matrix().astype(np.int)
    return X, X_test, y