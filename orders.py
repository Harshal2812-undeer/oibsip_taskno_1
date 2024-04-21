# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your data
df = pd.read_csv('/content/Orders.csv')

# Display the first 5 rows of the dataframe
print(df.head())

# Get a summary of the dataframe
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Descriptive statistics for categorical data
print(df.describe(include=[object]))

# Bar plots for each categorical attribute
for column in df.select_dtypes(include=[object]):
    df[column].value_counts().plot(kind='bar', title=column)
    plt.show()