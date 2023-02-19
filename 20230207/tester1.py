# from collections import Counter
#
# sample_string = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbccccccccddddddddddddddeeeeeeeeee'
#
# my_counter = Counter(sample_string)
# # print(my_counter) # mozhno indexirovat' kak slovar'
# # print(my_counter.most_common(1)[0][1])
# # print(list(my_counter.elements()))
#
# from collections import namedtuple
#
# Point = namedtuple('Point', 'x,y')
#
# # print(Point)
#
# pt = Point(-1, 2)
# print(pt)

from collections import OrderedDict

orderdict = OrderedDict()
orderdict['Name'] = 'Jack'
orderdict['Surname'] = 'Smith'

print(orderdict)