import csv

#Sample
data = [
    ['Alua', 87469566554],
    ['Aibek', 87074561245],
    ['Rasul', 84546544541]
]

# Open the CSV file in write mode
with open('sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['first_name', 'phone_number'])

    # Write the data rows
    for row in data:
        writer.writerow(row)