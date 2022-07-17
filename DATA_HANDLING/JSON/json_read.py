import json

with open("json_example.json", "r", encoding="UTF8") as f:
    contents = f.read()
    json_data = json.loads(contents)  # read -> loads

# print(type(json_data))
# print(json_data["employees"])

for employee in json_data["employees"]:
    print(employee)

for employee in json_data["employees"]:
    print(employee["lastName"])