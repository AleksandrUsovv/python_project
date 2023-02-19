import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers2 = [4, 5, 6, 7 , 8, 9]
names = ['Jack', 'Swen']
selections = [True, False, False, True]

res = itertools.compress(letters, numbers)
res2 = filter(lambda x: x > 2, numbers2)
print(list(res2))