import csv

output = open('./datasets/mycsv.csv', mode='w')

mywriter = csv.writer(output)

header = ['name', 'age']

mywriter.writerow(header)

data = ['Abdallah', 40]

mywriter.writerow(data)

output.close()