# 'r' - read
# 'a' - append
# 'w' - write
# 'x' = create
# 'r+' - read and write

# file = open('loren/loren.txt', 'r', encoding='UTF8')
# print(file.name)
# print(file.mode)
# print(file.encoding)
# print(file.closed)
# file.close()
# print(file.closed)
# with open('loren/loren.txt', 'r', encoding='UTF8') as file:
#
#     data = file.read()
#     print(len(data))
#     file.seek(0)
#     data = file.read()
#     print(len(data))
#    data = file.readline()
# print(data)
# print(type(data))
# # print(len(data))
#     chunk = 1000
#     data = file.read(chunk)
#     while len(data):
#         print(data)
#         data = file.read(chunk)





#C:\Users\Kasutaja\PycharmProjects\python_project\20230131\loren\loren.txt

#relative path
#20230131/loren/loren.txt
#
# import datetime
# dt = datetime.date.today()
# with open(f'loren/tester{dt}.txt', 'w', encoding='UTF8') as file:
#     file.write('Hello World!\n')
#     file.write('Hello Planet! ')
#     file.write(str(123))

# with open(f'loren/tester{dt}.txt', 'a', encoding='UTF8') as file:
#     file.seek(0)
#     file.write('Hello World!\n')
#     file.write('Hello Planet! ')
#     file.write(str(123))

# import datetime
# dt = datetime.date.today()
# with open(f'loren/loren.txt', 'r', encoding='UTF8') as read_file:
#     data = read_file.read()
#     with open(f'loren/tester.txt', 'w', encoding='UTF8') as file:
#         file.write(data.upper())

# with open(f'loren/testercreate.txt', 'x', encoding='UTF8') as file:
#     pass

# with open(f'files.py', 'r') as file:
#     data = file.read()
#
# print(data)

# with open(f'loren/testerveel.txt', 'r+', encoding='UTF8') as file:
#     data =  file.read()
#     print(data)
#     file.seek(0)
#     file.write(data.upper())

with open('loren/python.png', 'rb') as file:
    with open('loren/pythoncopy.png', 'wb') as wfile:
        data = file.read()
        wfile.write(data)