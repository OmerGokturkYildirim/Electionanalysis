# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.

#TRACK WINNING COUNTY AND VOTE COUNT


# Candidate options and candidate votes.
candidate_options = []
#I CREATE AN EMPTY LIST FOR COUNTIES
list_of_counties=[]
#I CREATE AN EMPTY DICTIONARY TO LEARN COUNTIES TOTAL VOTES
county_votes = {}
total_votes = 0
winning_count = 0


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    #I START A FOR LOOP TO FIND LIST OF COUNTIES AND COUNTY VOTES
    for row in file_reader:
        
        #I COUNT EACH VOTE
        total_votes += 1
        
        # I GET COUNTY NAME FROM EACH ROW
        county_name = row[1]
        
        #IF THE COUNTY DOESN'T MATCH ANY EXISTING COUNTY, ADD THE COUNTY LIST
        if county_name not in list_of_counties:
            # ADD THE COUNTY NAME TO THE COUNTY LIST
            list_of_counties.append(county_name)
            # TRACK COUNTIES' VOTER COUNT
            
            county_votes[county_name] = 0
        # ADD A VOTE TO COUNTY'S COUNT
        county_votes[county_name] += 1


with open(file_to_save, "w") as txt_file:
    # PRINTING THE FINAL VOTE COUNT TO THE TERMINAL
    county_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(county_results, end="")
    print(" \n")
    print("County Votes:\n")
     
    txt_file.write(county_results)
    
    for county in county_votes:
        #RETRIEVE VOTE COUNT AND PERCENTAGE
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
       
        if (votes > winning_count):
            winning_count = votes
            winning_county = county
            


    # PRINTING LARGEST COUNTY TURNOUT RESULT TO THE TERMINAL
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
      
        f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Save the final vote count to the text file.
  
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        
        txt_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    
    txt_file.write(winning_candidate_summary)