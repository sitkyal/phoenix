

# module to connect and load data

# Error Handling
# I/O Error, Bad File Name, Empty File,
# Wrong Extension, Bad File, Big File, Load Timeout

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
