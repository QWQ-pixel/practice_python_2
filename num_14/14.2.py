def passwrd():
    file_in, s = [], 's'
    while s != "":
        s = input()
        s = s.replace(':', ' ').replace(',', ' ')
        if s != "":
            file_in.append(s)
    passwords = input()
    passwords = passwords.replace(';', ' ')
    for i in file_in:
        list_ = i.split(sep=' ')
        if list_[1] in passwords:
            print("To:", list_[0], '\n'+list_[4], list_[5]+',', "ваш пароль слишком простой, смените его.")


passwrd()
