#PyPoll Challenge

#Import Modules
import os
import csv

#Set Variable for Pypoll data
# voters_candidates = []
# votes_per_candidate = []
vote_total = 0
candidate = ""
final_list = {}
winner_votes = 0
winner_name = ""

#Set path for csv file
election_data_csv_path = os.path.join("Resources/election_data.csv")

#Open and read csv

with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    #Read the header row
    csv_header = next(csvfile)
    # print(csv_header)

    #Loop through data
    for row in csv_reader:
        vote_total +=1

    #update candidates and their vote
        candidate = row[2]
        if candidate in final_list:
            final_list[candidate] += 1
        else:
            final_list[candidate] = 1
    #Printint initial results
    print(f"election results")
    print(f"-------------")
    print(f"total votes: {vote_total}")

    for candidate in final_list:

        #determine the percentage of candidate vote
        percentage = (final_list[candidate]/vote_total)*100
        percentage_formatted = "{:.3f}".format(percentage)
        print(candidate + ":" + str(percentage_formatted) + "%" + "(" + str(final_list[candidate])+")")
        #Calculate the number of votes
        if final_list[candidate] > winner_votes:
            winner_votes = final_list[candidate]
            winner_name = candidate
        print(winner_name)

    output = os.path.join("analysis", 'Electionresults.txt')
    with open(output, "w") as new_analysis:
        new_analysis.write("Election results")
        new_analysis.write("\n")
        new_analysis.write("--------------------")
        new_analysis.write ("Total votes")
        
        
    

    # #Sort the list in ascending order
    # sorted_list = sorted(voters_candidates)

    # #Arrange the sorted list by outcomes
    # arange_list = sorted_list

    # #count votes per candidates in most common outcome order
    # count_candidate = counter (arrange_list)
    # votes_per_candidate.append(count_candidate.most_common())

    # #Determine the percentage of votes per candidate in 3 digital points
    # for item in votes_per_candidate:

    #     first = format((item[0][1])*100/(sum(count_candidate.values())),'3f')
    #     second = format((item[1][1])*100/(sum(count_candidate.values())),'3f')
    #     third = format((item[2][1])*100/(sum(count_candidate.values())),'3f')
    #     fourth = format((item[3][1])*100/(sum(count_candidate.values())),'3f')

    #  #Print analysis
    # print("Election Results")
    # print("---------------------------")
    # print(f"Total Votes: {sum(count_candidate.values())}")
    # print("---------------------------")
    # print(f"{votes_per_candidate[0][0][0]}: {first}% {votes_per_candidate[0][0][1]})")
    # print(f"{votes_per_candidate[0][1][0]}: {first}% {votes_per_candidate[0][1][1]})")
    # print(f"{votes_per_candidate[0][2][0]}: {first}% {votes_per_candidate[0][2][1]})")
    # print(f"{votes_per_candidate[0][3][0]}: {first}% {votes_per_candidate[0][3][1]})")
    # print("---------------------------")
    # print(f"Winner: {votes_per_candidate[0][0][0]}")
    # print("---------------------------")
