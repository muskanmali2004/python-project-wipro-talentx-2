# 1. Differentiate between Python Array and NumPy Array?

# #--> Python Array:-
#   Feature    	   Python Array (from array module)	
# 1.Data Type	       Stores elements of a single, specific data type (e.g., all integers or all floats).
# 2.Functionality	   Basic array operations, but lacks advanced mathematical functions.
# 3.Performance	   Slower for numerical operations, as it is built on top of standard Python lists and doesn't offer vectorized operations.
# 4.Memory	       Less memory efficient for large datasets compared to NumPy arrays.
  

# #--> Numpy Array:-
#   Feature    	   Numpy Array (from array module)	
# 1.Data Type	       Stores elements of a single data type, but offers a much wider range of numeric types. 
# 2.Functionality	   Highly optimized for scientific computing and data manipulation. Provides extensive mathematical functions, linear algebra, and more.
# 3.Performance	   Much faster for numerical operations due to its C implementation and vectorized operations.
# 4.Memory           More memory efficient for large numerical datasets.








# 2. What is Numpy?
# NumPy is a fundamental Python library for scientific computing. 
# It provides a powerful N-dimensional array object (ndarray) and tools for working with these arrays.
# Its primary purpose is to efficiently handle numerical data and perform mathematical operations, 
# making it a cornerstone for data science and machine learning.










# 3. What are mathematical operations supported by Numpy?
# NumPy supports a vast range of mathematical operations, including:

# Arithmetic Operations: Addition, subtraction, multiplication, division, modulo, and exponentiation.

# Trigonometric Functions: sin(), cos(), tan(), etc.

# Logarithmic Functions: log(), log2(), log10(), etc.

# Statistical Operations: Mean, median, standard deviation, variance, percentiles, sum(), min(), max(), etc.

# Linear Algebra: Dot product, matrix multiplication, determinants, and eigenvectors.

# Comparison Operations: less(), greater(), equal(), etc.







# 4. How to detect the outliers using IQR?
# Outliers can be detected using the Interquartile Range (IQR) method. 
# First, calculate the first quartile (Q1) and the third quartile (Q3) of the data. 
# Then, compute the IQR as the difference between them (IQR=Q3−Q1). 
#  Outliers are defined as any data point that falls below the lower bound (Q1−1.5×IQR) or above the upper bound (Q3+1.5×IQR).






# 5. Why Pandas is used?
# Pandas is a popular Python library used for data manipulation and analysis. 
# It is built on top of NumPy and provides easy-to-use data structures like Series (1-D) and DataFrame (2-D) for handling structured data.
#  It's widely used because it simplifies tasks such as loading data from files, cleaning and preprocessing data, handling missing values, and performing statistical analysis.






# 6. What is Series in Pandas?
# A Pandas Series is a one-dimensional labeled array capable of holding data of any type. 
# It is similar to a column in a spreadsheet or a SQL table. 
# Each element in a Series has an associated label or index, 
# which can be used to access the data. 
# It is the fundamental building block for the more complex DataFrame object.







