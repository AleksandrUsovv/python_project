# def no_parameters():
#     # print('Hello world!')
#     return 'Hello world'
#
#
# def squares(number1, number2):
#     return number1 ** number2
#     # if number <0:
#     #     return ** 3
#     # return number ** 2
#
#
# no_parameters()
# print(no_parameters())
# squares(4, 4)
# print(squares(4, 4) - 6.7)

# def print_message(name, age, proffesion):
#     print(f'Hello {name}. You are {age} years old. You work as {proffesion}.')
#
# print_message('Alex', 19, 'boss')
# people = [('Roman', 34, 'lector'), ('Jack', 33,'Lisa')]
# for person in people:
#     print_message(person[0], person[1], person[2])

# a = 1
# b = 2
# c = 3
#
# def tester(a, b, c):
#     a = 10
#     b = 20
#     print(a, b, c)
#     return(a, b, c)
# a = 1
# b = 2
# c = 3
# print(a, b, c)
# tester(a, b, c)
# x = tester()
# print(x)

# def test123(a, b, c=1):
#     return a * b * c
#
# print(test123(10, 5, 3))

# def tester(a, b=1, *args, **kwargs):
#     print(a, b)
#     print(args)
#     for arg in args:
#         print(arg)
#     print(kwargs)
#
# tester(1, 1, 2, 2, 2, 2, 'hello', name='Alex', age=11)
#
# def say_hello():
#     print('Hello')
#
# def take_name(name):
#     say_hello()
#     print(name)
#
#
# take_name('Alex')
#
#
# def wrapper(f):
#     print('Starting work')
#     f()
#     print('Ending work')
#
# wrapper(say_hello)

import funcs
from funcs import double as dbl
print(dbl(3))