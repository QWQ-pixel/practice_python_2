def repost():
    num, rep, publ = int(input()), dict(), ''
    if 1 <= num <= 100:
        for i in range(num):
            string = input().replace(',', '').split()
            rep[string[0]] = int(string[-1])
            if i != 0:
                rep[string[4]] += int(string[-1])
                if i == num - 1:
                    rep[publ] += int(string[-1])
            elif i == 0:
                publ = string[0]
        print(*rep.values(), sep='\n')


repost()
