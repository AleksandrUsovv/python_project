# a = 'Hello'
# b = 'World'
#
# print(a, b, 23238, True, None, sep=', ', end='!\n')
# txt = 'Hello\nWorld'
# print(txt)
#
# print("that's'")
# print('that\'s')
# print("My favorite book is \"Metro2033\"")
# print('''That's ''')
# print(""" "metro2033" """)

salary = 2000
name = 'John'
age = 25
txt = '{0}\'s salary is {1}. He is {2} years old'
print(txt.format(name, salary, age))

product = 'computer'
price = 1000
txt2 = 'This {product:} costs {price:.2f}$.'
print(txt2.format(product=product, price=price))

x = 1234.459954305
y = 123.1223
print('the value of x is %.4f' % x)

emp_name = 'John'
emp_age = 15
emp_salary = 1000

print(f'Hi, my name is {emp_name.upper()}. I am {emp_age + 10}, my salary is {emp_salary:.2f}$')
