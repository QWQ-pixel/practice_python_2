def writer():
    string = input()
    strings = string.split(sep=' ')
    print(*strings, sep='\n')


writer()
