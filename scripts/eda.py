
# Error Handling
# Bad Column Name
# No data returned


# global import
import pandas as pd
import sys
import json


# preview data
# Mongo/text Stream


def fpreview_data(df):
    return df.head(n=5)

# identification of columns
# Mongo/text Stream


def fcolumns(df):
    cols = df.columns
    num_cols = df._get_numeric_data().columns
    cat_cols = list(set(cols) - set(num_cols))
    return cols, num_cols, cat_cols

# statistics
# Mongo/text Stream


def fstats(df, cols, num_cols):
    # stats for columns
    num_cols_stats = df.describe()
    cat_cols_stats = df.describe(include=['O'])

    # stats for categorical column leafs - leafs < 20
    leaf_count = {}
    for c in list(set(cols) - set(num_cols)):
        if df[c].unique().size < 20:
            leaf_count.update({c:df[c].value_counts().to_dict()})

#    leaf_count = [df[c].value_counts() for c in list(
#        set(cols) - set(num_cols)) if df[c].unique().size < 20]
    return num_cols_stats, cat_cols_stats, leaf_count

# Correlation matrix

def fcorr(df):
    col_corr = df.corr(method='pearson')
    return col_corr

