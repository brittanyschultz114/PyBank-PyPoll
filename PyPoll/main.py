import os
import csv

path = os.path.join('..', 'Resources', 'election_data.csv')

with open(path) as election:

    csvreader = csv.reader(election, delimiter=',')

    print('Election Results') 
    print('------------------------------------')
    
    next(csvreader)

    candidate = []
    results = []
    percent_votes = []
    total_votes = 0  

    for row in csvreader:
        total_votes += 1 

        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            results.append(1)
            
        else:
            index = candidate.index(row[2])
            results[index] += 1

    for votes in results:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    winner = max(results)
    index = results.index(winner)
    winning_candidate = candidate[index]
    
    print("Total Votes: ", str(total_votes))
    print('------------------------------------')
    for i in range(len(candidate)):
        print(f"{candidate[i]}: {str(percent_votes[i])} ({str(results[i])})")
    print('------------------------------------')
    print(f"Winner: {winning_candidate}")
    print('------------------------------------')


output_file = os.path.join('..', 'analysis', 'analysis.txt')


with open(output_file, "w", newline='') as txt_file:
    txt_file.write('Election Results\n')
    txt_file.write('------------------------------------\n')
    txt_file.write("Total Votes: " + str(total_votes))
    txt_file.write('\n')
    txt_file.write('------------------------------------\n')
    for i in range(len(candidate)):
        txt_file.write(f"{candidate[i]}: {str(percent_votes[i])} ({str(results[i])})" + "\n")
    txt_file.write('------------------------------------\n')
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write('------------------------------------\n')