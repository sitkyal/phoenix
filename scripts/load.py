

# module to connect and load data

# Error Handling
# I/O Error, Bad File Name, Empty File,
# Wrong Extension, Bad File, Big File, Load Timeout

import pandas as pd
import logging

def fload_csv(fname):
    try:
        print "Loading Data into frames....."
        df = pd.read_csv(fname)
        print " Data successfully loaded"
        return df, df.shape
    except EnvironmentError as e:
        logging.error(e)
#        error_log.write('An error occurred : %s\n' % e)
        return 1



def fload_xl(fname):
    try:
        pd.read_excel(fname, sheetname=1)
        print "Data successfully loaded"
        return df, df.shape
    except EnvironmentError as e:
        logging.error(e)
        return 1
