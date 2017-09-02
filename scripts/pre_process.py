# preprocessing


import pandas as pd
import sys
from label_features import flabel_features
from base_script_eda import fload_csv


def fpre_process(fname):
    # Hot encoding for all categorical columns
    # Impute values for nulls in categorical and numerical columns

    # 1. Get the selected labels and features
    # 2. Determine the cat / numerical in features
    # 3. Determine columns with Nulls
    # 4. Determine most frequent in Cat
    # 5. Impute cat column values with most frequent
    # 6. Detemine mean / average for Num
    # 7. Impute num column values with mean
    # 8. Standardize
    # 9. Return X and y

    # for testing
    label = pd.Series(['Survived'])
    features = pd.Series(['Pclass', 'Sex', 'Age'])

    selected_label, selected_features = flabel_features(label, features)

    # get the df from the loaded file
    df, size = fload_csv(fname)

    # calculate the numerical and cat columns

    cols = selected_features
    num_cols = df._get_numeric_data().cols
    cat_cols = list(set(cols) - set(num_cols))
    return cols, num_cols, cat_cols


fname = sys.argv[1]
print "sucessfull passing of " + fname
cols, num_cols, cat_cols = fpre_process(fname)
print cols, num_cols, cat_cols
