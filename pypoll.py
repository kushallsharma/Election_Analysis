# The data we need to retreive
# 1. total number of vote cast
# 2. A complete list of candidate received votes
# 3. The percentage of votes each candidate won
# 4. Total number of votes each candodate won
# 5. The winner of the election based on the popular votes


import csv
import os

# Variable declaration to load file

file_to_load = os.path.join("Resources","election_results.csv")

# Variable declaration to save into file

file_to_save = os.path.join("analysis","election_analysis.txt")

# Variable Declaration

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0.00

# Open election file and read it

with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)

    header = next(file_reader)
    
#Loop to analyse the file row by row

    for row in file_reader:
        total_votes +=1

        candidate_name = row[2]

        # Preparing candidate list

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        
        # Counting candidate's votes

        candidate_votes[candidate_name] += 1

    # Save results to text file
    
    with open(file_to_save,"w") as txt_file:

        # printing headers to screen and text file

        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")

        txt_file.write(election_results)

        # Loop for identifying the winner

        for candidates_name in candidate_votes:
            votes = candidate_votes[candidates_name]

            votes_percentage = (float(votes)/float(total_votes))*100
                    
            # printing each candidate results  to screen and text file

            candidate_results = (f"{candidates_name}: {votes_percentage: .2f}% ({votes})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

            if(votes>winning_count) and (votes_percentage>winning_percentage):
                winning_count = votes
                winning_percentage = votes_percentage
                winning_candidate = candidates_name
        
        # printing winning candidate results  to screen and text file

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate} \n"
            f"Winning Count {winning_count} \n"
            f"Winning Percentage {winning_percentage: .2f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)