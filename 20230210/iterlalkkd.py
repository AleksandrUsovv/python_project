import itertools

# counter = itertools.count()

# data = [100, 200, 300, 400]
# # daily_data = zip(counter, data)
# # print(list(daily_data))
#
# daily_data = itertools.zip_longest(data, range(10), fillvalue=False)
# print(list(daily_data))
# counter = itertools.count(start=-10.5, step=-0.5)
# counter = itertools.cycle([1, 2, 3])
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.cycle(['even', 'odd'])
#
# for x in range(100):
#     print(x, next(counter))

counter = itertools.repeat(2)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# result = map(lambda x, y: x ** y, range(100), itertools.repeat(2))
# for x in result:
#     print(x)

result = itertools.starmap(lambda x, y: x ** y, [(0, 2), (1, 2), (3, 5)])
for x in result:
    print(x)