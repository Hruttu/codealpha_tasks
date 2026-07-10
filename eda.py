# %% [markdown]
# # Task 2: Exploratory Data Analysis (EDA)
# Dataset: task2excel.csv
#
# Each "# %%" block is a runnable cell (Shift+Enter to run one at a time).

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Update this path to wherever your CSV lives on your machine
df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\projectFolder\task2excel.csv')
df.columns = [c.strip() for c in df.columns]
df.head(10)

# %% [markdown]
# ## 1. Explore data structure

# %%
print("Shape:", df.shape)
df.dtypes

# %%
df.describe()

# %%
df.describe(include='object')

# %%
for c in df.select_dtypes(include='object').columns:
    print(c, "->", df[c].unique())

# %% [markdown]
# ## 2. Data quality checks

# %%
print("Missing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# %%
# Convert order_date to a real datetime type
df['order_date'] = pd.to_datetime(df['order_date'])
print("Date range:", df['order_date'].min(), "to", df['order_date'].max())

# %% [markdown]
# ## 3. Validate assumptions
# Hypothesis: revenue = quantity * unit_price * (1 - discount)

# %%
df['calc_revenue'] = (df['quantity'] * df['unit_price'] * (1 - df['discount'])).round(2)
df['revenue_diff'] = (df['revenue'] - df['calc_revenue']).round(2)
df[['order_id', 'revenue', 'calc_revenue', 'revenue_diff']]

# %% [markdown]
# ## 4. Correlations

# %%
num_cols = ['quantity', 'unit_price', 'discount', 'delivery_days', 'customer_rating', 'revenue']
corr = df[num_cols].corr()
corr

# %%
plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Correlation Matrix of Numeric Variables')
plt.tight_layout()
plt.show()

# %% [markdown]
# ## 5. Group comparisons / trends

# %%
df.groupby('product_category')['revenue'].mean().sort_values(ascending=False)

# %%
df.groupby('region')['revenue'].mean().sort_values(ascending=False)

# %%
df.groupby('payment_method')['customer_rating'].mean().sort_values(ascending=False)


# ## 6. Visualizations

plt.figure(figsize=(6, 4))
df.groupby('product_category')['revenue'].mean().sort_values().plot(kind='barh', color='#4C72B0')
plt.title('Average Revenue by Product Category')
plt.xlabel('Avg Revenue')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(6, 4))
df.groupby('region')['revenue'].mean().sort_values().plot(kind='barh', color='#55A868')
plt.title('Average Revenue by Region')
plt.xlabel('Avg Revenue')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(6, 4))
sns.regplot(data=df, x='delivery_days', y='customer_rating', ci=None,
            scatter_kws={'s': 80, 'color': '#C44E52'})
plt.title('Delivery Days vs Customer Rating')
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(7, 4))
df_sorted = df.sort_values('order_date')
plt.plot(df_sorted['order_date'], df_sorted['revenue'], marker='o', color='#8172B2')
plt.title('Revenue Trend Over Time')
plt.xlabel('Order Date')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(6, 4))
df.groupby('payment_method')['customer_rating'].mean().sort_values().plot(kind='barh', color='#DD8452')
plt.title('Average Customer Rating by Payment Method')
plt.xlabel('Avg Rating')
plt.tight_layout()
plt.show()

