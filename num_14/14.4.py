def diagr():
    string = input()
    colm = string.split(sep=' ')
    w, h = len(colm), int(max(colm))
    print('*' * (w + 2))
    print('*' + ' ' * w + '*')
    for i in range(1, h + 1):
        print(end='*')
        for num in colm:
            if int(num) >= h - i + 1:
                print(end='*')
            else:
                print(end=' ')
        print('*')


diagr()
