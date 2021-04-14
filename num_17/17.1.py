def transliter():
    string, new_str = input().split(), ''
    for word in string:
        if word == string[-1]:
            new_str += change_lett(word)
        else:
            new_str += change_lett(word) + ' '
    print(new_str)


def change_lett(word):
    change_ = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
               'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
               'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
               'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
               'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia'}
    singh = [',', '?', ':', '!', '.']
    for letter in word:
        if letter in singh:
            pass
        elif letter.lower() != 'ь' and letter.lower() != 'ъ':
            if letter.islower():
                word = word.replace(letter, change_[letter.upper()].lower())
            else:
                word = word.replace(letter, change_[letter])
        else:
            word = word.replace(letter, '')
    return word


transliter()
