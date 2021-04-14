def fil():
    num, strings = int(input()), []
    for i in range(num):
        strings.append(input())
    for string in strings:
        if string[:4] != "####" and string[:2] != "%%":
            print(string)
        elif string[:2] == "%%":
            print(string[2:])


fil()
