
import csv
import os

file_to_load = os.path.join("Resources/election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")


#TRACK WINNING COUNTY AND VOTE COUNT


#I CREATE AN EMPTY LIST FOR CANDIDATES 
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
    #I PRINT THE FINAL VOTE COUNT TO THE TERMINAL
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
        #I RETRIEVE VOTE COUNT AND PERCENTAGE
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
       
        if (votes > winning_count):
            winning_count = votes
            winning_county = county
            


    #I PRINT LARGEST COUNTY TURNOUT RESULT TO THE TERMINAL
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
      
        f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)
candidate_votes = {}

# I TRACK THE WINNIG CANDIDATE, VOTE COUNT AND PERCENTAGE
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# I OPEN THE ELECTION RESULTS TO READ THE FILE.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
   
    headers = next(file_reader)
    # I PRINT EACH ROW IN THE CSV FILE
    for row in file_reader:
        # I ADD TO THE TOTAL VOTE COUNT
        total_votes += 1
        # I GET THE CANDIDATE NAME FROM EACH ROW
        candidate_name = row[2]
        # IF THE CANDIDATE DOES NOT MATCH ANY EXISTING CANDIDATE ADD THE CANDIDATE LIST
        if candidate_name not in candidate_options:
            # I ADD THE CANDIDATE NAME TO THE CANDIDATE LIST
            candidate_options.append(candidate_name)
            #I TRACK CANDIDATE'S VOTER COUNT
            candidate_votes[candidate_name] = 0
        # I ADD A VOTE TO THAT CANDIDATE'S COUNT
        candidate_votes[candidate_name] += 1
    

with open(file_to_save, "w") as txt_file:
    
    #I SAVE THE FINAL VOTE COUNT TO THE TEXT FILE
  
    for candidate in candidate_votes:
        # I RETRIEVE VOTE COUNT AND PERCENTAGE
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # I PRINT EACH CANDIDATE'S VOTER COUNT AND PERCENTAGE TO THE TERMINAL
        print(candidate_results)
        # I SAVE THE CANDIDATE RESULTS TO OUR TEXT FILE
        
        txt_file.write(candidate_results)
        
        # I DETERMINE WINNING VOTE COUNT, WINNING PERCENTAGE AND WINNING CANDIDATE
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # I PRINT THE WINNING CANDIDATE'S RESULTS TO THE TERMINAL
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # I SAVE THE WINNING CANDIDATE'S RESULTS TO THE TEXT FILE.
    
    txt_file.write(winning_candidate_summary)