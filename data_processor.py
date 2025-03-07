import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Separate numeric and non-numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    non_numeric_columns = df.select_dtypes(exclude=[np.number]).columns

    # Convert non-numeric data in numeric columns to NaN
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Handle missing values for numeric columns
    numeric_imputer = SimpleImputer(strategy='mean')
    print(f"Shape of numeric columns before imputation: {df[numeric_columns].shape}")
    numeric_data = numeric_imputer.fit_transform(df[numeric_columns])
    print(f"Shape of numeric data after imputation: {numeric_data.shape}")
    df[numeric_columns] = pd.DataFrame(numeric_data, columns=numeric_columns, index=df.index)

    # Handle missing values for non-numeric columns
    non_numeric_imputer = SimpleImputer(strategy='most_frequent')
    print(f"Shape of non-numeric columns before imputation: {df[non_numeric_columns].shape}")
    non_numeric_data = non_numeric_imputer.fit_transform(df[non_numeric_columns])
    print(f"Shape of non-numeric data after imputation: {non_numeric_data.shape}")
    df[non_numeric_columns] = pd.DataFrame(non_numeric_data, columns=non_numeric_columns, index=df.index)

    # Standardize numeric features
    scaler = StandardScaler()
    scaled_numeric_data = scaler.fit_transform(df[numeric_columns])
    print(f"Shape of numeric data after scaling: {scaled_numeric_data.shape}")
    df[numeric_columns] = pd.DataFrame(scaled_numeric_data, columns=numeric_columns, index=df.index)

    return df