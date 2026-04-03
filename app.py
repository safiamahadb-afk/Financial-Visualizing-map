import pandas as pd

# 1. This is our "Brain" - it decides the category
def categorize_expense(description):
    description = description.lower()
    if 'coffee' in description or 'chipotle' in description:
        return 'Food & Drink'
    elif 'shell' in description:
        return 'Transportation'
    elif 'netflix' in description:
        return 'Subscriptions'
    else:
        return 'Other'

# 2. Read the data
df = pd.read_csv('test_data.csv')

# 3. Apply the "Brain" to every row in our spreadsheet
df['Category'] = df['Description'].apply(categorize_expense)

print("--- Categorized Transactions ---")
print(df)

# 4. Group by Category and sum the amounts
summary = df.groupby('Category')['Amount'].sum()
print("\n--- Spending Summary ---")
print(summary)
import matplotlib.pyplot as plt

# Create a Pie Chart
summary.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Spending by Category')
plt.ylabel('')  # This hides the 'Amount' label on the side
plt.show()      # This actually opens the window with the chart