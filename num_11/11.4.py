def fix():
    for _ in range(int(input())):
        string, count = input(), 0
        if string[0] != '#':
            if '#' in string:
                if '\'' not in string[0:string.index('#')]:
                    string = string[0:string.index('#')]
            temp_list = string.split('\'')
            if len(temp_list) == 3:
                if '#' in temp_list[2]:
                    temp_list[2] = temp_list[2][0:temp_list[2].index('#')]
                temp_str = temp_list[2]
                temp_list2 = temp_str.split()
                temp_str = ' '.join(temp_list2)
                string = temp_str

                temp_str = temp_list[0]
                if temp_str.startswith(' '):
                    for letter in temp_str:
                        if letter == ' ':
                            count += 1
                        else:
                            break
                temp_list2 = temp_str.split()
                temp_str = ' '.join(temp_list2)
                string = ' ' * count + temp_str + '\'' + temp_list[1] + '\'' + string
            elif len(temp_list) == 1:
                if '#' in temp_list[0]:
                    temp_list[0] = temp_list[0][0:temp_list[0].index('#') + 1]
                string = temp_list[0]
                if string.startswith(' '):
                    for letter in string:
                        if letter == ' ':
                            count += 1
                        else:
                            break
                temp_list = string.split()
                string = ' ' * count + ' '.join(temp_list)
            print(string)


fix()
