def check():
    string, pos = input(), []
    string.split()
    for i in range(int(string.split()[0])):
        pos.append(input())
    res, mistake = calc(pos)
    print(int(string.split()[-1])-sum(res), '\n', *mistake)


def calc(strings):
    results, res, mistake = [], 1, []
    for string in strings:
        a = string.replace('*', ' ').split()
        num = string.replace('=', ' ').split()[-1]
        for i in a[:-1]:
            res *= int(i)
        if str(res) not in num:
            mistake.append(strings.index(string)+1)
        results.append(res)
        res = 1
    return results, mistake


check()
