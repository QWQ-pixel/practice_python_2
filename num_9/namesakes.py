def namesakes():
    num_employers, employers, counts, num = int(input()), list(), dict(), 0
    for i in range(num_employers):
        employers.append(input())
    for employer in employers:
        counts[employer] = counts.get(employer, 0) + 1
    values = list(counts.values())
    print(values)
    for value in values:
        if value != 1:
            num += value
    print(num)


namesakes()

