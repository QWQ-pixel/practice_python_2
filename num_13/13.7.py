def dead(n):
    list_solders, sort_ = [], []
    for i in range(n):
        list_solders.append(input())
    number = int(input())
    while len(list_solders) > 0:
        index = 0
        for _ in list_solders:
            if index < len(list_solders):
                sort_.append(list_solders[index])
                index += number
        for solder in sort_:
            if solder in list_solders:
                list_solders.remove(solder)
    print(*sort_, sep='\n')


if __name__ == "__main__":
    num = int(input())
    if num > 0:
        dead(num)
