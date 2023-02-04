import csv
import sys

# with open('test.csv', 'r', encoding='utf8') as csv_file:
#     pass
#
# x = [1, 2, 3, 4 ,5]
# y = iter(x)
# print(y)
#
# for i in y:
#     print(i)

# print(next(y)) # с итератором выдает по очереди
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))


# with open('test.csv', 'r', encoding='utf8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # print(csv_reader)
#     col_name = next(csv_reader) # метод некст убрал строчку с названием столбцов
#     for line in csv_reader:
#         print(line)

# with open('test.csv', 'r', encoding='utf8') as csv_file:
#     csv_reader = list(csv.reader(csv_file))
#     print(csv_reader)

# with open('test.csv', 'r', encoding='utf8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('test_copy.csv', 'w', encoding='utf8') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='/', lineterminator='\n')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

# with open('test.csv', 'r', encoding='utf8') as new_file:
#     csv_reader = csv.reader(new_file, delimiter='.')
#     for x in csv_reader:
#         print(x)

with open('test.csv', 'r', encoding='utf8') as new_file:
    csv_reader = csv.DictReader(new_file, fieldnames=['NM', 'DOB', 'TOWN'])
    for line in csv_reader:
        print(line)

with open('test_copy.csv', 'w', encoding='utf8') as wfile:
    csv_writer = csv.DictWriter(wfile, lineterminator='\n', fieldnames=['Name', 'Date of Birth', 'Town'])

    csv_writer.writeheader()
    for line in csv_reader:
        csv_writer.writerow(line)