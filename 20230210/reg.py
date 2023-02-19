import re

with open('people.txt', 'r', encoding='utf8') as file:
    data = file.read()

name_pattern = re.compile(r'([A-Za-z]+ [A-Za-z-]+)\n')
address_pattern = re.compile(r'\d{3} [0-9A-Za-z\'-]+ St\., [A-Za-z\' -]+ [A-Z]{2} \d{5}')
matches1 = name_pattern.findall(data)
print(len(matches1))

matches2 = address_pattern

people_pairs = list(zip(matches1, mat))