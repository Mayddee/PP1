import csv

# Sample data
data = [
    ['Madina', 87078556123],
    ['Aselya', 87751252525],
    ['Ansar', 87774126541]
]

# Open the CSV file in write mode
with open('table.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['first_name', 'phone_number'])

    # Write the data rows
    for row in data:
        writer.writerow(row)
