import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD THE EXCEL DATA
# ==========================================
# Replace 'your_cleaned_data.xlsx' with your actual file name.
# If your data is on a specific sheet, add: sheet_name='YourSheetName'
file_name = 'your_cleaned_data.xlsx'
df = pd.read_excel("Cleaned Data.xlsx")

print("Data loaded successfully!")
print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")

# ==========================================
# 2. BASIC DATA INSPECTION
# ==========================================
print("--- FIRST 5 ROWS ---")
print(df.head())
print("\n--- DATA TYPES & MISSING VALUES ---")
print(df.info())
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe(include='all')) # Includes both numeric and text summaries

# Automatically separate numeric and categorical columns for plotting
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

# ==========================================
# 3. VISUALIZATIONS
# ==========================================

# Chart 1: Distribution of the first numeric column found
if len(numeric_cols) > 0:
    target_num_col = numeric_cols[0]
    plt.figure(figsize=(8, 4))
    sns.histplot(df[target_num_col], kde=True, color='skyblue')
    plt.title(f'Distribution of {target_num_col}')
    plt.xlabel(target_num_col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
else:
    print("\n  No numeric columns found for distribution plotting.")

# Chart 2: Count plot for the first categorical column found
if len(categorical_cols) > 0:
    target_cat_col = categorical_cols[0]
    plt.figure(figsize=(8, 4))
    # Taking top 10 categories if there are too many to prevent crowding
    top_categories = df[target_cat_col].value_counts().head(10).index
    sns.countplot(data=df[df[target_cat_col].isin(top_categories)], y=target_cat_col, order=top_categories, palette='viridis')
    plt.title(f'Top Categories in {target_cat_col}')
    plt.tight_layout()
    plt.show()
else:
    print("\n No categorical columns found for count plotting.")

# Chart 3: Correlation Heatmap (Only if there are 2 or more numeric columns)
if len(numeric_cols) >= 2:
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[numeric_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap of Numeric Variables')
    plt.tight_layout()
    plt.show()
else:
    print("\n Not enough numeric columns to generate a correlation heatmap.")