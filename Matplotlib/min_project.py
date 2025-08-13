# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # 1. Create a sample dataset for demonstration
# data = {'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
#         'Value1': np.random.randint(1, 100, 12),
#         'Value2': np.random.randint(50, 150, 12),
#         'Group': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']}
# df = pd.DataFrame(data)

# print("Sample Dataset:")
# print(df)
# print("-" * 30)

# # 2. Basic Data Information
# # Get a quick overview of the data
# print("Data Info:")
# df.info()
# print("-" * 30)

# # Get descriptive statistics for numerical columns
# print("Descriptive Statistics:")
# print(df.describe())
# print("-" * 30)

# # 3. Data Visualization with Matplotlib and Seaborn
# # Set the style for the plots
# sns.set_style("whitegrid")

# # Create a figure with subplots
# fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# fig.suptitle('Exploratory Data Analysis Visualizations', fontsize=16)

# # --- Plot 1: Histogram to show the distribution of 'Value1' ---
# # A histogram helps visualize the frequency distribution of a numerical variable.
# sns.histplot(df['Value1'], bins=5, kde=True, ax=axes[0, 0], color='skyblue')
# axes[0, 0].set_title('Distribution of Value1')

# # --- Plot 2: Box plot to detect outliers in 'Value2' ---
# # A box plot is excellent for showing the distribution and identifying potential outliers.
# sns.boxplot(x='Value2', data=df, ax=axes[0, 1], color='salmon')
# axes[0, 1].set_title('Box Plot of Value2')

# # --- Plot 3: Bar plot to compare the average of 'Value1' by 'Category' ---
# # A bar plot is great for comparing categorical data.
# sns.barplot(x='Category', y='Value1', data=df, ax=axes[1, 0], palette='viridis')
# axes[1, 0].set_title('Average Value1 by Category')

# # --- Plot 4: Scatter plot to show the relationship between 'Value1' and 'Value2' ---
# # A scatter plot helps visualize the relationship between two numerical variables.
# sns.scatterplot(x='Value1', y='Value2', hue='Group', data=df, ax=axes[1, 1], style='Group')
# axes[1, 1].set_title('Value1 vs Value2 by Group')

# # Adjust layout to prevent titles from overlapping
# plt.tight_layout(rect=[0, 0, 1, 0.96])
# plt.show()