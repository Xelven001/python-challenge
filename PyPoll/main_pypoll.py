#import proper modules for analysis 
import pandas as pd 
from pathlib import Path
import sys
stdout_default = sys.stdout 

#define input and output files for reading/writing
file = Path('Resources/election_data.csv')
file_output = "../PyPoll/Analysis/output.txt"

#read csv file with panda module and filter out for neccessary columns 
df = pd.read_csv(file)
df = df[['Candidate','Ballot ID']]

#create group by Candidate to get votes per Candidate 
df_grp = df.groupby('Candidate').count()

#rename columns for readability 
df_grp = df_grp.rename(columns={"Ballot ID":"All Votes"})

#Add percent column using based on existing "All Votes" Column
df_grp['Pecent of All Votes'] = df_grp['All Votes'].apply(lambda x: (x / df_grp['All Votes'].sum()) * 100).round(3)

#Count all votes to get total (here for ref but no variable created as code is used in print function)
df_grp['All Votes'].sum()

#define winner for output
winner_index = df_grp["All Votes"].idxmax()


#Output - Open output file / redirect standard output using sys/ write print statements to new .txt file 
with open(file_output, "w") as file:
    sys.stdout = file  # Now print statements will write to the file
    # Your print statements here
    print("\nElection Results")
    print(f"\n-----------------------")
    print(f"\nTotal Votes: {df_grp['All Votes'].sum()}")
    print(f"\n-----------------------")
    print(f"")

    for index, row in df_grp.iterrows(): 
        candidate = index
        votes = int(row["All Votes"])
        percent = row["Pecent of All Votes"]
        print(f"{index}: {percent}% ({votes})")
    print(f"\n-----------------------")
    print(f"\nWinner: {winner_index}!! Congrats!!")

#reset standard output to terminal   
sys.stdout = stdout_default

#reprint results to terminal 
print("\nElection Results")
print(f"\n-----------------------")
print(f"\nTotal Votes: {df_grp['All Votes'].sum()}")
print(f"\n-----------------------")
print(f"")

for index, row in df_grp.iterrows(): 
    candidate = index
    votes = int(row["All Votes"])
    percent = row["Pecent of All Votes"]
    print(f"{index}: {percent}% ({votes})")
print(f"\n-----------------------")
print(f"\nWinner: {winner_index}!!")


#Thank you! 
