


def fload_csv(fname):
    import pandas as pd
    df = pd.read_csv(fname)
    print fname + " successfully loaded"
    return df, df.shape
