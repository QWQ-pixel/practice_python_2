def letter():
    msg, num, let = input(), int(input()), input()
    if len(let) > 1 or num-1 > len(msg):
        print("ОШИБКА")
    else:
        if msg[num-1] == let:
            print("ДА")
        else:
            print("НЕТ")


letter()
