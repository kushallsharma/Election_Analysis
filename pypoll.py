import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")

file_to_save = os.path.join("analysis","election_analysis.txt")

with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)

    header = next(file_reader)
    print(header)
# The data we need to retreive
# 1. total number of vote cast
# 2. A complete list of candidate received votes
# 3. The percentage of votes each candidate won
# 4. Total number of votes each candodate won
# 5. The winner of the election based on the popular votes