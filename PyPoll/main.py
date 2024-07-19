import csv
import os

# Function to analyze election data
def analyze_pypoll(csvfile):
    # Check if the file exists
    if not os.path.exists(csvfile):
        print(f"Error: File '{csvfile}' not found.")
        return
    
    # Initialize variables
    total_votes = 0
    candidates = {}
    winner = {"name": "", "votes": 0}

    # Read CSV file
    with open(csvfile, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)  # Store the header row
        
        for row in reader:
            # Calculate total votes
            total_votes += 1
            
            # Extract candidate name from row
            candidate_name = row[2]
            
            # Count votes for each candidate
            if candidate_name in candidates:
                candidates[candidate_name] += 1
            else:
                candidates[candidate_name] = 1
    
    # Determine the winner
    for candidate, votes in candidates.items():
        if votes > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = votes
    
    # Calculate percentage of votes for each candidate
    results = "Election Results\n" + "-" * 25 + "\n"
    results += f"Total Votes: {total_votes}\n" + "-" * 25 + "\n"
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
    results += "-" * 25 + "\n"
    results += f"Winner: {winner['name']}\n"
    results += "-" * 25 + "\n"
    
    # Print results to terminal
    print(results)
    
    # Write results to text file
    with open("election_results.txt", 'w') as output_file:
        output_file.write(results)

# Main execution
if __name__ == "__main__":
    # Specify the correct path to election_data.csv
    csv_path = 'C:/Users/Jean/Documents/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv'
    
    # Call analyze_pypoll function with the correct path
    analyze_pypoll(csv_path)
