import json


with open("../datasets/customer.json", "r") as f:
    data = json.load(f)
    data['records'][0]

print(data)