def func():
    string = input()
    letters_patt = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '],
                    'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
                    'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   ']}
    for letter in string:
        for key in letters_patt.keys():
            if letter == key:
                print(*letters_patt.get(key), sep='\n')


func()
