import os
import csv

# Path to collect data from the Resources folder
electiondata = os.path.join('..', 'Resources', 'election_data.csv')

candidates = []


# Read in the CSV file
with open(electiondata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    count = 0
    countli = 0
    countkhan = 0
    countcorrey = 0
    countotooley = 0
    # Loop through the data
    for row in csvreader:
        count += 1

        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] == "Li":
            countli += 1
        elif row[2] == "Khan":
            countkhan += 1
        elif row[2] == "Correy":
            countcorrey += 1
        elif row[2] == "O'Tooley":
            countotooley += 1

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {str(count)}")
    print("-------------------------")
    print(f"{candidates[0]}: {float(round(((countkhan/count)*100),2))}% ({str(countkhan)})")
    print(f"{candidates[1]}: {float(round(((countcorrey/count)*100),2))}% ({str(countcorrey)})")
    print(f"{candidates[2]}: {float(round(((countli/count)*100),2))}% ({str(countli)})")
    print(f"{candidates[3]}: {float(round(((countotooley/count)*100),2))}% ({str(countotooley)})")
    print("-------------------------")
    print(f"Winner: Khan") #fix hard code, how to reference the winning amount
    print("-------------------------")

output_path = os.path.join("..", "Output", "PyPoll.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Total Votes: ' + str(count)])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow([candidates[0] + ': ' + str(float(round(((countkhan/count)*100),2))) + '% (' + (str(countkhan)) + ')'])
    csvwriter.writerow([candidates[1] + ': ' + str(float(round(((countcorrey/count)*100),2))) + '% (' + (str(countcorrey)) + ')'])
    csvwriter.writerow([candidates[2] + ': ' + str(float(round(((countli/count)*100),2))) + '% (' + (str(countli)) + ')'])
    csvwriter.writerow([candidates[3] + ': ' + str(float(round(((countotooley/count)*100),2))) + '% (' + (str(countotooley)) + ')'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Winner: Khan']) #fix hard code, how to reference the winning amount
    csvwriter.writerow(['-------------------------'])
