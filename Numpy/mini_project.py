import numpy as np

# Sample data
data = np.array([2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 50])

# Calculate Q1 and Q3
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

# Calculate the Interquartile Range (IQR)
IQR = Q3 - Q1

# Define the upper and lower bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = [x for x in data if x < lower_bound or x > upper_bound]

print(f"Sample Data: {data}")
print(f"First Quartile (Q1): {Q1}")
print(f"Third Quartile (Q3): {Q3}")
print(f"IQR: {IQR}")
print(f"Lower Bound: {lower_bound}")
print(f"Upper Bound: {upper_bound}")
print(f"Outliers: {outliers}")

# A more direct way to get outliers using numpy
outlier_indices = np.where((data < lower_bound) | (data > upper_bound))
print(f"Outliers (using numpy.where): {data[outlier_indices]}")