import json

with open('sample2.json', 'r', encoding='utf8') as file:
    data = json.load(file)

for person in data['people']:
    if person['has_licence'] == False:
        data['people'].remove(person)

with open('sample2_copy.json', 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2)