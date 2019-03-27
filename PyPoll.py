
# import the needed modules
import os
import csv 

# setting up the path of the diretly to read the csv file
file_path = 'election_data.csv'

# initializing the needed variables
total_votes = 0

# election result dictionary
election_results = {}

# readindg the rows of the csv file  
with open(file_path) as file_handler:
     data_lines = csv.reader(file_handler)

# skipping the header row
     first_row = next(data_lines)
 
# generating the election results dictionaly 
     for row in data_lines:
          candidate_name = row[2]
          total_votes = total_votes + 1
          if candidate_name not in election_results.keys():
               election_results[candidate_name] = 1 
          else:
               election_results[candidate_name] += 1       
     
# writing/creating a text file for the results
text_file = open("election_results.txt", "w") 

# printing header & total number of votes
print("Election Results", file = text_file)
print("---------------------------", file = text_file)
print("Total Votes: " + str(total_votes), file = text_file)
print("---------------------------", file = text_file)

# initializing a value to determine the winter instead of using max
winner_votes = 0
winner_name = ""

# looping to calculate candidate percentages and print the election results
for key, value in election_results.items():
# fining the winter name and theb total of his votes
     if election_results[key] > winner_votes:
          winner_votes = election_results[key]
          winner_name = key

     candidate_percentage = (election_results[key]/total_votes) * 100
     candidate_per = "%3.3f"% (candidate_percentage)
     print(key + ":  " + candidate_per + "%  (" + str(value) +")", file = text_file)


print("---------------------------", file = text_file)
print("Winner:  " + winner_name, file = text_file)
print("---------------------------", file = text_file)