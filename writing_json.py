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


# 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
#
# git remote set-url origin https://marijawo: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
# @github.com/marijawo/data_eng_with_python.git
