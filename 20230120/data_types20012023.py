# empty_lst = []
# print(type(empty_lst))

#empty_lst1 = list() # объявление пустого списка

world = 'world'

# # filled_lst = [123, 0.123, True, 'Hello baby!', [1, [9, 9, 9, 9], 3, 4]]
# # print(len(filled_lst))
# # print(filled_lst[-1][1][1] + 20)
# # print(filled_lst[-1][1][1].upper())

courses = ['history', 'math', 'litereture', 'physics', 'programming']
nums = [1, 5, 6, 8, 3, 4, 2]
#print(courses[::-1])

# courses[4] = 'art'
# print(courses)

# adding nethods
# courses.append('art')
# print(courses)
# courses.extend(['art', 'english'])
# print(courses)
# courses.insert(0, 'sport')
# print(courses)

# courses.remove('math') # deleting only one time
# print(courses)
# popped = courses.pop(0)
# print(courses)
# print(popped)

#courses.reverse()
#print(list(reversed(courses)))

# courses.sort() #sorting by unicode => a>A
# print(courses)

# nums.sort(reverse=True)
# print(nums)

# print(sorted(courses))

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# print(courses.index('math'))
# print('math' in courses)
# print(8 in nums)

# courses_str = str(courses)
# print(courses_str)

# courses_str = '*'.join(courses)
# print(courses_str)
# new_lst = courses_str.split('*')
# print(new_lst)
#
# print(courses + nums)

# courses2 = courses
# courses2[0] = 'art'
# courses[1] = 'english'
# print(courses)
# print(courses2) # mutatuon!!!

# courses2 = courses.copy()
# courses2[0] = 'art'
# courses[1] = 'english'
# print(courses)
# print(courses2)
# print(id(courses))
# print(id(courses2))

# empty_tup = tuple(courses)
# print(empty_tup.index('math'))
# print(empty_tup.count('math'))
#
# one = (1,)
# print(one)
# print(type(one))

# empty_set = set()
# print(empty_set)
# print(type(empty_set))

# courses = {'history', 'math', 'litereture', 'physics', 'programming'}
# courses2 = {'sport', 'Lalalala'}
# nums = {1, 5, 6, 8, 3, 4, 2}

# courses.remove('math')
# x= courses.pop()
# print(courses)
# print(x)
#
# y = ['one', 'two', 'three', 'one', 'two']
# print(list(set(y)))

# courses.add('art')
# print(courses)

# courses.update(['art', 'english'])
# print(courses)
# courses.clear()
# print(courses)

# print(courses.union(courses2))
# print(courses.intersection(courses2))

# print(courses.difference(courses2))
#
# list()
# tuple()
# set() # удалятся дубликаты

# for i in courses:
#     if i == 'math':
#         print('Math sucks')
#     else:
#         print(i.upper())
#
# pairs = [[1, 'one'], [2, 'two'], [3, 'three']]
# for num, word in pairs:
#     print(num)
#     print(word)

pairs = [['jack', 'johns', 21], ['two', 'smith', 22], ['three', 'petrov', 29]]
for first, last, age in pairs:
    print(f'Hello {first} {last}. your age is {age}')

for num1 in range(10):
    for num2 in range(10):
        for num3 in range(10):
            for num4 in range(10):
                print(num1, num2, num3, num4)