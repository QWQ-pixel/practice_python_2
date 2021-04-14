def brain_():
    s = input()
    k, m, n = 0, 0, 0
    lent = [0] * 30000
    for i in s:
        if i == "[":
            m += 1
        elif i == ']':
            n += 1
        if m - n > 0:
            if i == '+' and lent[k] != 0:
                lent[k] += 1
            elif i == '-' and lent[k] != 0:
                while lent[k] != 0:
                    lent[k] -= 1
                    lent[k] = lent[k] % 256
        elif i == '>':
            k += 1
        elif i == '<':
            k -= 1
        elif i == '+':
            lent[k] += 1
        elif i == '-':
            lent[k] -= 1
            lent[k] = lent[k] % 256
        elif i == '.':
            print(lent[k])


brain_()
