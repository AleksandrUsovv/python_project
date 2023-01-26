x = 5
empty_dict = {'name': 'Roman', 'surname': 'Kutselepa', 1: 'one', x: 'Five',
              'lst': [1, 2, 3, 4], 'dct': {'one': 1, 'two': 2}}
# print(empty_dict.get('job', False))

empty_dict['lol'] = 'Jack'
# empty_dict.update(name='Jacky')
empty_dict.update({'name': 'Jacky', 'surname': 'Popapap', 'job': 'artist'})

x = empty_dict.pop('name')
del empty_dict['surname']
print(empty_dict)
print(x)

print(empty_dict.keys())
print(empty_dict.values())
print(empty_dict.items())

for key, val in empty_dict.items():
    print(key)
    print(val)
    print()
