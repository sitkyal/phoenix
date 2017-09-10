
# Instructions
# Run the followng on CLI or Node
# python base_script_eda.py train.csv


# global import
import pandas as pd
import sys
import json

# load cvs and run status


def fload_csv(fname):
    import pandas as pd
    df = pd.read_csv(fname)
    print fname + " successfully loaded"
    return df, df.shape

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

    # stats for categorical column leafs - leafs < 10
    leaf_count = [df[c].value_counts() for c in list(
        set(cols) - set(num_cols)) if df[c].unique().size < 10]
    return num_cols_stats, cat_cols_stats, leaf_count

# Run the main script

with open('config.json') as input_file:
        data = json.load(input_file)

fname = str(data['filename'])

#fname = sys.argv[1]
df, size = fload_csv(fname)
preview = fpreview_data(df)
cols, num_cols, cat_cols = fcolumns(df)
num_cols_stats, cat_cols_stats, leaf_count = fstats(df, cols, num_cols)


base_eda_out = {
    "File Name": fname,
    #"Preview Data": preview,
    "Columns": cols,
    "Numerical Columns": num_cols,
    "Categorical Columns": cat_cols,
    "Num Column Stats": num_cols_stats,
    "Cat Column Stats": cat_cols_stats
}

print base_eda_out
sys.stdout.flush()
