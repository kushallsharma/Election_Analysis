import csv
import os



file_to_load = os.path.join("Resources","election_results.csv")

file_to_save = os.path.join("analysis","election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0.00

with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)

    header = next(file_reader)
    
    for row in file_reader:
        total_votes +=1

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
        
    for candidates_name in candidate_votes:
        votes = candidate_votes[candidates_name]

        votes_percentage = (float(votes)/float(total_votes))*100
                
        print(f"{candidates_name}: {votes_percentage: .2f}% ({votes})")

        if(votes>winning_count) and (votes_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = candidates_name
        
    print("-----------------------------")
    print(f"Winner: {winning_candidate} \nWinning Count {winning_count} \nWinning Percentage {winning_percentage: .2f}%")
    print("-----------------------------")









# The data we need to retreive
# 1. total number of vote cast
# 2. A complete list of candidate received votes
# 3. The percentage of votes each candidate won
# 4. Total number of votes each candodate won
# 5. The winner of the election based on the popular votes