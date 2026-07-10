# # Task 3: Data Visualization — Step by Step
# Dataset: task2excel.csv (same data used in Task 2)

# %% [markdown]
# ## STEP 0 — Load the data (needed before any visual can be made)

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\projectFolder\task 3 folder\task2excel.csv')          # <-- update path if needed
df.columns = [c.strip() for c in df.columns]
df['order_date'] = pd.to_datetime(df['order_date'])
df.head()

# %% [markdown]
# ## REQUIREMENT 1: "Transform raw data into visual formats like charts, graphs, and dashboards"
#
# This is the core transformation: numbers in a table -> shapes on a chart.
# Below, raw columns (product_category, revenue) are aggregated with pandas,
# then handed to matplotlib/seaborn to become a bar chart.

# %%
category_revenue = df.groupby('product_category')['revenue'].mean().sort_values()
print(category_revenue)   # <- still just numbers here

plt.figure(figsize=(6, 4))
category_revenue.plot(kind='barh', color=['#8A8F87', '#B4622E', '#2F5233'])
plt.title('Average Revenue by Product Category')
plt.xlabel('Average Revenue ($)')
plt.tight_layout()
plt.savefig('chart1_category_revenue.png', dpi=150)   # <- now it's a visual artifact
plt.show()

# %% [markdown]
# ## REQUIREMENT 2: "Use tools like Matplotlib, Seaborn, or Tableau for creating visuals"
#
# Everything in this script uses matplotlib (plt) and seaborn (sns) directly.
# Below are a few different chart TYPES from those libraries, to show range —
# a line chart, a scatter chart with a regression line, and a heatmap.

# %%
# Line chart (matplotlib)
df_sorted = df.sort_values('order_date')
plt.figure(figsize=(7, 4))
plt.plot(df_sorted['order_date'], df_sorted['revenue'], marker='o', color='#2F5233')
plt.title('Daily Revenue Trend')
plt.xlabel('Order Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart2_revenue_trend.png', dpi=150)
plt.show()

# %%
# Scatter chart with regression line (seaborn)
plt.figure(figsize=(6, 4))
sns.regplot(data=df, x='delivery_days', y='customer_rating', ci=None,
            scatter_kws={'s': 80, 'color': '#B4622E'}, line_kws={'color': '#8A8F87'})
plt.title('Delivery Days vs Customer Rating')
plt.tight_layout()
plt.savefig('chart3_delivery_vs_rating.png', dpi=150)
plt.show()

# %%
# Heatmap (seaborn)
num_cols = ['quantity', 'unit_price', 'discount', 'delivery_days', 'customer_rating', 'revenue']
plt.figure(figsize=(6, 5))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('chart4_correlation_heatmap.png', dpi=150)
plt.show()

# %% [markdown]
# ## REQUIREMENT 3: "Design visuals that enhance understanding and reveal insights clearly"
#
# Design choices that make a chart clearer, not just present:
# - explicit titles that state the finding, not just the variable names
# - sorted bars (smallest to largest) so the ranking is instantly visible
# - a distinct highlight color for the value that matters most
# - axis labels with units ($ signs, day counts, etc.)

# %%
region_revenue = df.groupby('region')['revenue'].mean().sort_values()

# Highlight the top region in a different color so the eye goes there first
colors = ['#8A8F87'] * len(region_revenue)
colors[-1] = '#2F5233'   # highlight the highest-revenue region

plt.figure(figsize=(6, 4))
region_revenue.plot(kind='barh', color=colors)
plt.title('South Region Generates the Most Average Revenue')   # <- states the insight
plt.xlabel('Average Revenue ($)')
plt.tight_layout()
plt.savefig('chart5_region_revenue_highlighted.png', dpi=150)
plt.show()

# %% [markdown]
# ## REQUIREMENT 4: "Craft compelling data stories that support decision-making"
#
# A story = an intentional ORDER of charts + a written takeaway after each one,
# not just charts dumped side by side. Below, we print short narrative text
# after each analysis, the same way you'd caption charts in a report or slide deck.

# %%
top_category = category_revenue.idxmax()
top_region = region_revenue.idxmax()
corr = df['delivery_days'].corr(df['customer_rating'])

print(f"""
DATA STORY
----------
1) Revenue is concentrated: '{top_category}' is the strongest category,
   and the '{top_region}' region brings in the most revenue on average.

2) Revenue has no clear trend across the 9 days observed — it's driven by
   individual large orders, not steady growth.

3) Delivery speed matters to customers: delivery_days and customer_rating
   have a correlation of {corr:.2f}, meaning slower delivery tends to come
   with lower satisfaction.

DECISION IMPLICATION:
Prioritizing faster delivery and doubling down on the '{top_category}'
category in the '{top_region}' region are the two clearest, data-backed
levers available from this dataset.
""")

# %% [markdown]
# ## REQUIREMENT 5: "Build a strong portfolio with impactful and well-designed visualizations"
#
# A portfolio piece = your charts saved as real files, not just shown once in
# a notebook and lost. Every chart above already called plt.savefig(), so by
# this point you have PNGs on disk. Below, we just confirm what's saved.

# %%
import os
saved_charts = [f for f in os.listdir('.') if f.startswith('chart') and f.endswith('.png')]
print("Portfolio-ready chart files saved:")
for f in saved_charts:
    print(" -", f)

print("""
Next steps to finish the portfolio piece:
  - Drop these PNGs into a Word doc / PDF / slide deck with the narrative
    text from Requirement 4 next to each chart.
  - Or combine them into a single dashboard image / webpage.
  - Upload the notebook (.ipynb) or script (.py) itself to GitHub so the
    code is visible too, not just the output.
""")