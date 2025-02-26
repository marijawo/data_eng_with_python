import pandas as pd
import json

# Read JSON file properly
with open('../datasets/customer.json', 'r') as file:
    data = json.load(file)

# Normalize JSON into a DataFrame
df = pd.json_normalize(data, record_path='records')

# Convert DataFrame to JSON
json_output = df.head(2).to_json()

print(json_output)
