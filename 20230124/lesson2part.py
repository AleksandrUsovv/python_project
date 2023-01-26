# people = [('Jack', 'Smith', 18), ('Mary', 'Gold', 20)]
#
# for person in people:
#     print(person)
#
# for name, surname, age in people:
#     print(name, surname, age)

# while True:
#     print('none stop')
# x = 0
# while x<100:
#     print('XxxX', x)
#     x += 1

# dist_to_target = 1567
# current_pos = 0
# step = 0.6
# cnt = 0
# while current_pos < dist_to_target:
#     print(cnt)
#     current_pos += step
#     cnt += 1

# for x in range(10):
#     if x == 5:
#         continue
#     if x == 8:
#         break
#     print(x)
#
# cnt = 0
# while True:
#     print(cnt)
#     if cnt == 100:
#         break
#     cnt += 1

# try:
#     user_input = float(input('enter: '))
# except:
#     print('Must enter number')
# else:
#     print(user_input ** 2)
# finally:
#     print('goodbye')
while True:
    try:
        user_id = input('Please enter you ID code: ')
        int(user_id)
        if len(user_id) != 11:
            raise Exception
    except valueerror:
        print('code error')
        continue
    except Exception:
        if len(user_id) > 11:
            print('too long')
        else:
            print('too short')
        continue
    else:
        print('your id is', user_id)
        break

        # user_choice_2 = input("Please choose:\n1.Print 1 'If you would like to continue'\n"
        #                       "2.Exit\n--> ")
        # if user_choice_2 == '1':
        #     continue
        # elif user_choice_2 == '2':
        #     break
        #     print('Goodbye')
        # else:
        #     print('Choice is out of range!')
        #     # print('New Cycle')