# preprocessing


import pandas as pd
import numpy as np
import sys
import json
import logging


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
    # 10. Return X and y - Done
    # 11. Include label in the pre-process

    preprocess_logger = logging.getLogger('lpreproc')

    try:
        preprocess_logger.info('Preprocessing started')
        # Get the labels and features selected
        from label_features import flabel_features
        olabel, ofeatures = flabel_features()

        def load_process():

            preprocess_logger.info('Data load started')
            from load import fload_csv
            df, size = fload_csv(fname)
        # Store in temp dataframe
            tdf = df[ofeatures].copy()
            ldf = df[olabel].copy()

            preprocess_logger.info('Data load ended')
            return tdf, ldf

        def null_process(tdf, ldf):
            # calculate the numerical and cat columns
            preprocess_logger.info('Imputing null values')
            cols = list(tdf.columns)
            num_cols = list(tdf._get_numeric_data().columns)
            cat_cols = list(set(cols) - set(num_cols))

        # Determine columns with Null values and Replace NAs

            null_num_cols = tdf[num_cols].columns[tdf[num_cols].isnull().any()
                                              ].tolist()
            null_cat_cols = tdf[cat_cols].columns[tdf[cat_cols].isnull().any()
                                              ].tolist()

        # For numerical columns

            for col in null_num_cols:
                tdf[col].fillna(tdf[col].mean(), inplace=True)

        # For categorical columns impute and hot encode
            preprocess_logger.info('Hot Encoding categorical features')

            for col in null_cat_cols:
            # impute missing values
                tdf[col].fillna(tdf[col].value_counts().max(), inplace=True)

            for col in cat_cols:
            # Hot Encode
                tdf = pd.concat([tdf, pd.get_dummies(tdf[col])], axis=1)

            tdf.drop(cat_cols, axis=1, inplace=True)
            return tdf, ldf


    # Program execution

        # Load Data
        tdf, ldf = load_process()

        # Null and Hot Encoding
        tdf, ldf  = null_process(tdf, ldf)

        # Extract X and y
        y = ldf.as_matrix().astype(np.float)
        X = tdf.as_matrix().astype(np.float)

        # reshape for cross validation - sheez!
        c, r = y.shape
        y = y.reshape(c,)

        preprocess_logger.info('Preprocessing ended')

        return X, y
    except Exception as e:
        preprocess_logger.exception(e)
        return 1
        sys.exit(1)


#fname = sys.argv[1]
#X, y = fpre_process(fname)
# print X, y
# sys.stdout.flush()
