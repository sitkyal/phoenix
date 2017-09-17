

# module to connect and load data

import pandas as pd

def fload_csv(fname):
    print "Loading Data into frames....."
    df = pd.read_csv(fname)
    print " Data successfully loaded"
    return df, df.shape

def fload_xl(fname):
    pd.read_excel(fname, sheetname=1)
    print "Data successfully loaded"
    return df, df.shape
