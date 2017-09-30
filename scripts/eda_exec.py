
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
from load import fload_csv, fload_xl
from eda import fpreview_data, fcolumns, fstats, fcorr


# Run the main script

with open('config.json') as input_file:
        data = json.load(input_file)

fname = str(data['filename'])

#fname = sys.argv[1]
df, size = fload_csv(fname)
preview = fpreview_data(df)
cols, num_cols, cat_cols = fcolumns(df)
num_cols_stats, cat_cols_stats, leaf_count = fstats(df, cols, num_cols)
col_corr = fcorr(df)


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
col_corr.to_csv('output/' + fname + '_correlation.csv', index=True)

num_cols_stats.to_csv('output/' + fname + '_numcolstats.csv', index=True)
cat_cols_stats.to_csv('output/' + fname + '_catcolstats.csv', index=True)

pd.DataFrame.from_dict(leaf_count).to_csv('output/' + fname + '_leafcount.csv', index=True)

# JSON output

with open('output/' + fname + '_cols.json', 'w') as outfile:
    json.dump(columns_json, outfile)

with open('output/' + fname + '_preview.json', 'w') as outfile:
    json.dump(preview.to_dict(orient = 'index'), outfile)

with open('output/' + fname + '_correlation.json', 'w') as outfile:
    json.dump(col_corr.to_dict(orient = 'index'), outfile)

with open('output/' + fname + '_numcolstats.json', 'w') as outfile:
    json.dump(num_cols_stats.to_dict(orient = 'dict'), outfile)

with open('output/' + fname + '_catcolstats.json', 'w') as outfile:
    json.dump(cat_cols_stats.to_dict(orient = 'dict'), outfile)

with open('output/' + fname + '_leafcount.json', 'w') as outfile:
    json.dump(leaf_count, outfile)

sys.stdout.flush()
