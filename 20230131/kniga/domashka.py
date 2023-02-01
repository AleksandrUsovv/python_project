with open(f'trimushketera.txt', 'r', encoding='UTF8') as read_file:
    data = read_file.read()
    slova = data.split()

    print('Общее кол-во слов :', len(slova))

    unique_slova = list(slova)

    def unique_words(unique_slova):
        unique = []

        for i in unique_slova:
            if i in unique:
                continue
            else:
                unique.append(i)
        return unique

    unik = str(unique_words(unique_slova))
    unik2 = unik.split()
    print('Общее кол-во уникальных слов :', len(unik2))

    for unik3 in unik2:
        print(sorted(unik3.split()))


    with open(f'kol_vo.txt', 'w', encoding='UTF8') as file:
        file.write(str(len(slova)))
        file.write(' - Общее кол-во слов\n')
        file.write(str(len(unik2)))
        file.write(' - Общее кол-во уникальных слов\n')

