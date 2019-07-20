import pandas as pd
import numpy as np

def add(a, b):
  return a + b

def impute_nans(df, columns):
  for column in columns:
    processed_data = pd.DataFrame({})
    processed_data[column] = df[column].fillna(df[column].dropna().median())
  return processed_data