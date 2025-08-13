import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# 1. Create a sample dataset (similar to what you might find in a real project)
data = {'Country': ['France', 'Spain', 'Germany', 'Spain', 'Germany', 'France', 'Spain', 'France', 'Germany', 'France'],
        'Age': [44, 27, 30, 38, 40, 35, np.nan, 48, 50, 37],
        'Salary': [72000, 48000, 54000, 61000, 62000, 58000, 52000, 79000, 83000, 67000],
        'Purchased': ['No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']}
df = pd.DataFrame(data)

print("Original Data:\n", df)
print("-" * 30)

# --- Handling Missing Values ---
# We will fill the missing 'Age' value (NaN) with the mean of the 'Age' column.
# The 'SimpleImputer' from scikit-learn is a powerful way to handle this.
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df['Age'] = imputer.fit_transform(df[['Age']])

# In this simple example, we can also manually impute the value.
# df['Age'].fillna(df['Age'].mean(), inplace=True)

print("Data after handling missing values:\n", df)
print("-" * 30)

# --- Handling Categorical Data ---
# 'Country' and 'Purchased' are categorical columns and need to be encoded.
# We will use 'OneHotEncoder' for 'Country' and 'LabelEncoder' for 'Purchased'.

# For 'Purchased' (Yes/No), LabelEncoder is sufficient.
label_encoder = LabelEncoder()
df['Purchased'] = label_encoder.fit_transform(df['Purchased'])

# For 'Country' (multiple categories), OneHotEncoder is better to avoid ordinality issues.
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), ['Country'])],
    remainder='passthrough'
)
df_transformed = ct.fit_transform(df)
df_transformed = pd.DataFrame(df_transformed, columns=['Country_France', 'Country_Germany', 'Country_Spain', 'Age', 'Salary', 'Purchased'])

print("Data after encoding categorical features:\n", df_transformed)
print("-" * 30)

# --- Feature Scaling ---
# We will standardize the numerical columns ('Age' and 'Salary') so they have a mean of 0 and a standard deviation of 1.
# This is a critical step for many machine learning algorithms.

scaler = StandardScaler()
# We scale only the numerical columns.
df_transformed[['Age', 'Salary']] = scaler.fit_transform(df_transformed[['Age', 'Salary']])

print("Final Preprocessed Data after scaling:\n", df_transformed)