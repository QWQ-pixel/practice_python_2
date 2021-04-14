def recep():
    num, string = int(input()), ''
    for i in range(num):
        wrd = input()
        if 'лук' not in wrd:
            string += wrd
            if i < num - 1 and i != 0:
                string += ', '
            else:
                string += '.'
    print(string)


recep()
