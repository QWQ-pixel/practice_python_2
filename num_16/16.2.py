def csv_2_0():
    strings, steps = [], []
    for i in range(int(input())):
        strings.append(input())
    for i in range(int(input())):
        steps.append(input())
    for step in steps:
        print(strings[int(step[0])].split(',')[int(step[-1])])


csv_2_0()


