import json

with open("File/data.json", "r") as f:
    data = json.load(f)
    print(data)

with open("File/data.json", "w") as f:
    json.dump({"name": "John", "age": 30, "city": "New York"}, f)
    print("Data written to JSON file.")
    