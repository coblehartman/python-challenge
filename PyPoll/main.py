import os
import csv

# File path to the election data CSV file
file_path = '/Users/coblehartman/Documents/Berkeley/Module Challenges/module-challenge-three/python-challenge/PyPoll/Resources/election_data.csv'

# Dictionary to store candidate votes
candidate_votes = {}

# Variables to store total votes and winner information
total_votes = 0
winner_votes = 0
winner = ""

# Read the CSV file and calculate the required values
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Determine the winner and calculate vote percentages
output_text = "Election Results\n-------------------------\n"
output_text += f"Total Votes: {total_votes}\n-------------------------\n"

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    output_text += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

output_text += f"-------------------------\nWinner: {winner}\n-------------------------\n"

# Print the analysis to the terminal
print(output_text)

# Export the results to a text file
output_file = '/Users/coblehartman/Documents/Berkeley/Module Challenges/module-challenge-three/python-challenge/PyPoll/analysis/election_results.txt'
with open(output_file, 'w') as file:
    file.write(output_text)

print(f"Analysis has been exported to {output_file}")
