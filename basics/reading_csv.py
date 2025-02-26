import csv

with open('../datasets/customer.csv', newline='') as f:
    myreader = csv.DictReader(f)  # Instantiate DictReader with the file object
    headers = next(myreader)  # Get the first row (column headers)

    for row in myreader:
        print(row['name'])  # Access the 'name' column
