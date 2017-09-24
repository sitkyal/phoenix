
# Error Handling
# I/O Error, Bad File Name, Empty File,
# Wrong Extension, Bad File, Big File, Load Timeout
# Bad Column Name
# No data returned
# Cannot write file to db / file system


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

    # stats for categorical column leafs - leafs < 20
    leaf_count = {}
    for c in list(set(cols) - set(num_cols)):
        if df[c].unique().size < 20:
            leaf_count.update({c:df[c].value_counts().to_dict()})

#    leaf_count = [df[c].value_counts() for c in list(
#        set(cols) - set(num_cols)) if df[c].unique().size < 20]
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


# prep data for output
columns_json = {}
columns_csv = []

for col in num_cols:
    columns_json.update({col:"N"})
    columns_csv.append([col, "N"])
for col in cat_cols:
    columns_json.update({col : "C"})
    columns_csv.append([col, "C"])


# CSV output

columns_csv = pd.DataFrame(data=columns_csv, columns=[
                           'Column', 'Type'])
columns_csv.to_csv('output/' + fname + '_columns.csv', index=False)

preview.to_csv('output/' + fname + '_preview.csv', index=False)

num_cols_stats.to_csv('output/' + fname + '_numcolstats.csv', index=False)
cat_cols_stats.to_csv('output/' + fname + '_catcolstats.csv', index=False)

pd.DataFrame.from_dict(leaf_count).to_csv('output/' + fname + '_leafcount.csv', index=False)

# JSON output

with open('output/' + fname + '_cols.json', 'w') as outfile:
    json.dump(columns_json, outfile)

with open('output/' + fname + '_preview.json', 'w') as outfile:
    json.dump(preview.to_dict(orient = 'index'), outfile)

with open('output/' + fname + '_numcolstats.json', 'w') as outfile:
    json.dump(num_cols_stats.to_dict(orient = 'dict'), outfile)

with open('output/' + fname + '_catcolstats.json', 'w') as outfile:
    json.dump(cat_cols_stats.to_dict(orient = 'dict'), outfile)

with open('output/' + fname + '_leafcount.json', 'w') as outfile:
    json.dump(leaf_count, outfile)

sys.stdout.flush()
