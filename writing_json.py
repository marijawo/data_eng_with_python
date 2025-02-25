from faker import Faker
import json

output = open('./datasets/customer.json', 'w')
fake = Faker()


all_data={}

all_data['records'] = []

for x in range(1000):
    data ={"name":fake.name(),
           "age":fake.random_int(min=18, max=80),
           "street":fake.street_address(),
           "city":fake.city(),
           "zip":fake.zipcode(),
           "lng":float(fake.longitude()),
           "lat": float(fake.latitude())}
    all_data['records'].append(data)

json.dump(all_data, output)

