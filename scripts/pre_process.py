# preprocessing


import pandas as pd
import numpy as np
import sys


def fpre_process(fname):
    # Hot encoding for all categorical columns
    # Impute values for nulls in categorical and numerical columns

    # 1. Get the selected labels and features - Done
    # 2. Determine the cat / numerical in features - Done
    # 3. Determine columns with Nulls - Done
    # 4. Determine most frequent in Cat - Done
    # 5. Impute cat column values with most frequent - Done
    # 6. Detemine mean / average for Num - Done
    # 7. Impute num column values with mean - Done
    # 8. Hot Encode - Done
    # 9. Standardize - TBD
    # 10. Return X and y - To be Done

    # olabel, ofeatures = flabel_features(ilabel, ifeatures) # uncomment when testing is done

    # for testing - Replace this code with extracting from label_features.py
    olabel = ['Survived']
    ofeatures = ['Pclass', 'Sex', 'Age', 'Embarked', 'Cabin']

    from load import fload_csv

    df, size = fload_csv(fname)

    # calculate the numerical and cat columns

    cols = list(df[ofeatures].columns)
    num_cols = list(df[ofeatures]._get_numeric_data().columns)
    cat_cols = list(set(cols) - set(num_cols))

    # Determine columns with Null values and Replace NAs

    null_num_cols = df[num_cols].columns[df[num_cols].isnull().any()].tolist()
    null_cat_cols = df[cat_cols].columns[df[cat_cols].isnull().any()].tolist()

    # For numerical columns

    for col in null_num_cols:
        df[col].fillna(df[col].mean(), inplace=True)

    # For categorical columns impute and hot encode

    for col in null_cat_cols:

        # impute missing values

        df[col].fillna(df[col].value_counts().max(), inplace=True)

    for col in cat_cols:
        # Hot Encode

        df = pd.concat([df, pd.get_dummies(df[col])], axis=1)

    # Extract X and y
    y = df[olabel] #.as_matrix().astype(np.float)
    X = df[ofeatures]# .as_matrix().astype(np.float)

    return df, y, X


fname = sys.argv[1]
print "sucessfull passing of " + fname
df, y, X = fpre_process(fname)
print df.shape, X['Cabin'].unique()
