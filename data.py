import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open("data.json", 'w') as file:
    json.dump(data, file)

with open("data.json", 'r') as file:
    data = json.load(file)
print(data)