def saving_money():
    num, table = int(input()), [[]]
    for i in range(num - 1):
        table.append([int(j) for j in input().split()])
    stations = input().split()
    station_1, station_2 = int(stations[0]), int(stations[1])
    w = table[max(station_1, station_2)][min(station_1, station_2)]
    b = -1
    for i in range(num):
        if i != station_1 and i != station_2:
            if w > table[max(station_1, i)][min(station_1, i)] + table[max(i, station_2)][min(i, station_2)]:
                w = table[max(i, station_2)][min(i, station_2)] + table[max(i, station_2)][min(i, station_2)]
                b = i
    if b != -1:
        print(b)
    else:
        print(station_1)


saving_money()
