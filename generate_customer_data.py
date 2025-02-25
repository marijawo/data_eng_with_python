from faker import Faker
import csv

output = open('datasets/customer.csv', 'w')
fake = Faker()

header = ['name', 'age', 'city', 'state', 'zip', 'lng', 'lat']
my_writer = csv.writer(output)
my_writer.writerow(header)

for r in range(1000):
    my_writer.writerow([fake.name(), fake.random_int(min=18, max=80), fake.street_name(), fake.city(), fake.state(), fake.zipcode(), fake.longitude(), fake.latitude()])
