# 1. What is Data Preprocessing?
# Data Preprocessing is a crucial step in data science where raw data is transformed into a clean, usable, and efficient format for analysis or machine learning models. 
# Raw data is often incomplete, inconsistent, or contains errors, which can negatively affect a model's performance.
# Preprocessing involves a series of steps to fix these issues.








# 2. Difference between Data Wrangling and Data Preprocessing.

# While the terms are often used interchangeably, they have slightly different scopes.
# --> Data Wrangling is a broader term that encompasses all activities involved in transforming and mapping data from a "raw" format to another format, 
# often with the intent of making it more appropriate and valuable for a variety of downstream purposes like analytics. 
# It includes tasks like data acquisition, parsing, joining, and aggregating.

# --> Data Preprocessing is a subset of data wrangling that focuses on preparing data specifically for machine learning algorithms. 
# It includes tasks like handling missing values, encoding categorical variables, feature scaling, and feature engineering.





# 3. How to handle missing values?

# Missing values can be handled in several ways:
# 1. Deletion: Remove the rows or columns with missing data. This is simple but can lead to a loss of valuable information.

# 2. Imputation: Fill the missing values with a substitute.
#     -->Mean/Median/Mode Imputation: Replace missing values with the mean, median, or mode of the column.
#     -->Constant Value Imputation: Replace missing values with a constant number (e.g., 0).
#     -->Advanced Imputation: Use more sophisticated methods like K-Nearest Neighbors (KNN) or regression to predict and fill the missing values.





# 4. What is Data Imputation?
# Data imputation is the process of replacing missing values (often denoted as NaN or null) in a dataset with a substitute value. 
# Instead of deleting data points, which can lead to a loss of information, imputation preserves the dataset's size while still addressing the missing data problem. 
# The goal is to estimate the missing value as accurately as possible, using methods like mean, median, or more complex machine learning models.








# 5. How to handle inappropriate Data

# "Inappropriate data" is a general term that can refer to several issues, including:
# -->Outliers: Data points that are significantly different from others. They can be handled by deletion or transformation (e.g., using log transformation).
# -->Incorrect Data Types: For example, a numerical column stored as text. This is handled by type casting (e.g., using pd.to_numeric in Pandas).
# -->Inconsistent Data: Values with different formats (e.g., "USA" vs. "United States"). This is handled by standardizing the values.
# # -->Duplicate Rows: Identical rows that should be removed. This is handled by using a drop_duplicates() function.-->
# -->Irrelevant Features: Columns that don't contribute to the model. These can be removed to improve performance and reduce complexity.