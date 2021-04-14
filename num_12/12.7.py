def scale(n_, m_):
    strings = []
    for i in range(n_):
        strings.append(input())
    a, b = round(n_ / 2), round(m_ / 2)
    strings = change_string(n_, m_, a, b, strings)
    print(*strings, sep='\n')


def change_string(n_, m_, a, b, strings):
    count, res = 0, []
    for i in range(n_ - a):
        if count > len(strings):
            break
        res.append(strings[count])
        count += 2
    return change_symbols(m_, b, res)


def change_symbols(m_, b, strings):
    count, res, new_string = 1, [], ''
    for string in strings:
        for i in range(m_ - b):
            new_string = string[::2]
        res.append(new_string)
    return res


if __name__ == "__main__":
    n, m = int(input()), int(input()),
    scale(n, m)
