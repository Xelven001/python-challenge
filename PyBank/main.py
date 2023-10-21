import pandas as pd 
from pathlib import Path

file = Path('Resources/budget_data.csv')

df = pd.read_csv(file)

# Verified no dupe month rows
# df['Date'].nunique() == df['Date'].count()

total_months = df['Date'].nunique()
total = df["Profit/Losses"].sum()
mean = df["Profit/Losses"].mean()

difference = df["Profit/Losses"].diff()
average_change = difference.mean().round(2)


df["Difference"]= df["Profit/Losses"].diff().fillna('0').astype('int64')


increase_row = df[df['Difference'] == df['Difference'].max()]
increase_date = increase_row['Date'].to_string(index=False)
increase_amt =  increase_row['Difference'].to_string(index=False)

decrease_row = df[df['Difference'] == df['Difference'].min()]
decrease_date = decrease_row['Date'].to_string(index=False)
decrease_amt =  decrease_row['Difference'].to_string(index=False)

print("Financial Analysis")
print("\n---------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {increase_date}(${increase_amt})')
print(f'Greatest Decrease in Profits: {decrease_date}(${decrease_amt})')





