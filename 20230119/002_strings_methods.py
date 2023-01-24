string_sample1 = 'Hello world world'
                #Отчет с нуля
                #0123456
                #символы в обратном порядке -3 -2 -1 (но лучше избегать)
string_sample2 = 'first letteR is lowercase'
string_sample3 = ' extra whitespaces     *      '
german_sample = 'der Fluß'

#[Start:End:Step]
print(string_sample1[-1])
print(string_sample1[6:11])
print(string_sample1[:5])
print(string_sample1[::2])
print(string_sample1[5:11:2])
print(string_sample1[::-1])

print(len(string_sample1))
print(string_sample1[len(string_sample1) - 1])

print(string_sample1.upper())
#string_sample1 = string_sample1.upper()

print(german_sample.lower())
print(german_sample.casefold())

print(string_sample2.capitalize())
print(string_sample2.title())

print(string_sample3.strip()) #только в начале и конце строки, по умолчанию пробел. но можно задать символы
print(string_sample3.rstrip('* '))
print(string_sample3.lstrip('* '))

print(string_sample1.replace('world', 'planet',1))
print(string_sample1.replace('  ',' ').capitalize())

print(string_sample1.split(', '))

a, b, c = string_sample1.split()
print(a)
print(b)
print(c)

# a, b, c = input('please enter').split()
# print(a)
# print(b)
# print(c)

print(string_sample1.count('o'))
print(string_sample1.find('world'))

print('world' in string_sample1)