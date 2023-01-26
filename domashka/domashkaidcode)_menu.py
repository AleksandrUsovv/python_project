while True:
    user_input = input("Please choose:\n1.Print 1 'Validation ID_code and getting data'\n2.Print 2 to Exit\n--> ")
    if user_input == '2':
        print('Good bye!')
        break
    elif user_input == '1':
        user_id = input('Please enter your ID_Code ')
        try:
            int(user_id)
            if len(user_id) != 11:
                raise UserWarning
        except ValueError:
            print('ID_CODE ERROR!')
        except UserWarning:
            if len(user_id) > 11:
                print('ID_CODE is too long')
            else:
                print('ID_CODE is too short')
            continue
        else:
            if user_id[0] == '1':
                xxyy_birth = '18'
                gender = 'Male'
            elif user_id[0] == '2':
                xxyy_birth = '18'
                gender = 'Female'
            elif user_id[0] == '3':
                xxyy_birth = '19'
                gender = 'Male'
            elif user_id[0] == '4':
                xxyy_birth = '19'
                gender = 'Female'
            elif user_id[0] == '5':
                xxyy_birth = '20'
                gender = 'Male'
            elif user_id[0] == '6':
                xxyy_birth = '20'
                gender = 'Female'
            else:
                xxyy_birth = 'NO_DATA'
                gender = 'NO_DATA'

            byear = user_id[1:3]
            bmonth = user_id[3:5]
            bday = user_id[5:7]

            if int(user_id[7:10]) in range(1, 11):
                region = 'Kuressaare haigla'
            elif int(user_id[7:10]) in range(11, 20):
                region = 'Tartu Ülikooli Naistekliinik'
            elif int(user_id[7:10]) in range(21, 151):
                region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
            elif int(user_id[7:10]) in range(151, 161):
                region = 'Keila haigla'
            elif int(user_id[7:10]) in range(161, 221):
                region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
            elif int(user_id[7:10]) in range(221, 271):
                region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
            elif int(user_id[7:10]) in range(271, 371):
                region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
            elif int(user_id[7:10]) in range(371, 421):
                region = 'Narva haigla'
            elif int(user_id[7:10]) in range(421, 471):
                region = 'Pärnu haigla'
            elif int(user_id[7:10]) in range(471, 491):
                region = 'Haapsalu haigla'
            elif int(user_id[7:10]) in range(491, 521):
                region = 'Järvamaa haigla (Paide)'
            elif int(user_id[7:10]) in range(521, 571):
                region = 'Rakvere haigla, Tapa haigla'
            elif int(user_id[7:10]) in range(571, 601):
                region = 'Valga haigla'
            elif int(user_id[7:10]) in range(601, 651):
                region = 'Viljandi haigla'
            elif int(user_id[7:10]) in range(651, 701):
                region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
            else:
                region = 'NO_DATA'

            while True:
                user_input_2 = input("Please choose:\n1.Show gender:\n"
                                  "2.Show date of birth\n"
                                  "3.Show region of birth\n"
                                  "4.Validation ID_CODE\n"
                                  "0.Exit\n--> ")
                if user_input_2 == '1':
                    if gender != 'NO DATA':
                        print(f'Gender: {gender}')
                    else:
                        print('NO DATA')
                elif user_input_2 == '2':
                    if xxyy_birth != 'NO DATA':
                        print(f'DOB: {bday}.{bmonth}.{xxyy_birth + byear}')
                    else:
                        print('NO DATA')
                elif user_input_2 == '3':
                    if region != 'NO DATA':
                        print(f'You were born in {region}.')
                    else:
                        print(f'NO DATA')
                elif user_input_2 == '4':
                    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                    result = 0
                    cnt = 0
                    for num in chk1:
                        result += num * int(user_id[cnt])
                        cnt += 1
                    if result % 11 == int(user_id[10]):
                        print('ID is valid!')
                    else:
                        result = 0
                        cnt = 0
                        for num in chk2:
                            result += num * int(user_id[cnt])
                            cnt += 1
                        if result % 11 == int(user_id[10]):
                            print('ID is valid!')
                        else:
                            print('ID is not valid!')
                elif user_input_2 == '0':
                    print('Good bye')
                    quit()
                else:
                    print('Choice is out of range!')
    else:
        print('Choice is out of range!')
        print('New Cycle')