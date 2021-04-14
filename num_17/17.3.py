def hbd():
    num, bd, d = int(input()), dict(), dict()
    if 1 <= num <= 100:
        for _ in range(num):
            string = input().split()
            key = string[0] + ' ' + string[1]
            bd[key] = string[-1]
        num = int(input())
        months = [input() for _ in range(num)]
        list_key = list(bd.keys())
        list_key.sort(reverse=True)
        for i in list_key:
            d[i] = bd[i]
        for month in months:
            if month in d.values():
                print(get_key(d, month))
            else:
                print()


def get_key(d, value):
    key = ''
    for k, v in d.items():
        if v == value:
            key += k+' '
    return key.strip()


hbd()
