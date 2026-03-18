import pandas as pd

def remove_duplicates(df):
    return df.drop_duplicates()

def fill_missing(df, method='ffill'):
    return df.fillna(method=method)

def drop_missing(df):
    return df.dropna()

def summary(df):
    print("\nSummary:")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Missing values:\n", df.isnull().sum())