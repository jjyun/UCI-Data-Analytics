import os
import csv

# Path to collect data from the Resources folder
budget = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    count = 0
    total = 0
    max = 0
    min = 0
    profit = 0

    # Loop through the data
    for row in csvreader:
        #average block
        count += 1
        total += int(row[1])

        #max min block
        if int(row[1]) > max:
            max = int(row[1])
        if int(row[1]) < min:
            min = int(row[1])
        totalchange = max - min

        #Greatest increase pseudo block
        # Create a variable
            # == profit
        # iterate through the array finding the difference between n+1 and n.
            # == within the for loop going row by row. row[1] is the column but
            # how do we get the next value?
        # if this value is greater than the original value of the variable
            #if difference > Profit
        #     then set the variable to this new value
        #       == profit = difference
        #Apply logit to get decrease, flip inequality


    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(count)}")
    print(f"Total: ${str(total)}")
    print(f"Average  Change: ${str(totalchange/count)}")
    print(f"Greatest Increase in Profits: ")
    print(f"Greatest Decrease in Profits: ")

output_path = os.path.join("..", "Output", "PyBank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months: ' + str(count)])
    csvwriter.writerow(['Total: $' + str(total)])
    csvwriter.writerow(['Average  Change: $' + str(totalchange/count)])
    csvwriter.writerow(['Greatest Increase in Profits: '])
    csvwriter.writerow(['Greatest Decrease in Profits: '])
