#import proper modules for analysis 
import pandas as pd 
from pathlib import Path
import sys
stdout_default = sys.stdout 

#define input and output files for reading/writing
file = Path('Resources/budget_data.csv')
file_output ="../PyBank/Analysis/output.txt"

#read csv file with panda module 
df = pd.read_csv(file)

# Verified no dupe month rows
# df['Date'].nunique() == df['Date'].count()

#calculate requested agg functions 
total_months = df['Date'].nunique()
total = df["Profit/Losses"].sum()
mean = df["Profit/Losses"].mean()

#use .diff to create difference object and perform mean calculateion for avg change
difference = df["Profit/Losses"].diff()
average_change = difference.mean().round(2)

#Add new Difference column and fill empty cells with 0. Also converts column to int
df["Difference"]= df["Profit/Losses"].diff().fillna('0').astype('int64')

#Use Min/Max to find the top increase and botom decrease rows 
increase_row = df[df['Difference'] == df['Difference'].max()]
increase_date = increase_row['Date'].to_string(index=False)
increase_amt =  increase_row['Difference'].to_string(index=False)

decrease_row = df[df['Difference'] == df['Difference'].min()]
decrease_date = decrease_row['Date'].to_string(index=False)
decrease_amt =  decrease_row['Difference'].to_string(index=False)

with open(file_output, "w") as file:
    sys.stdout = file  # Now print statements will write to the file
    print("Financial Analysis")
    print("\n---------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {increase_date}(${increase_amt})')
    print(f'Greatest Decrease in Profits: {decrease_date}(${decrease_amt})')

#reset standard output to terminal   
sys.stdout = stdout_default

#reprint results to terminal 
print("Financial Analysis")
print("\n---------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {increase_date}(${increase_amt})')
print(f'Greatest Decrease in Profits: {decrease_date}(${decrease_amt})')





