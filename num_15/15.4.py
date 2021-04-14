def f():
    num_str, numbers, mods, medians, all_numbers = int(input()), [], [], [], []
    for i in range(num_str):
        numbers.append(input())
    for s in numbers:
        num = s.split()
        all_numbers.extend(num)
        mods.append(mod(num))
        medians.append(med(num))
    print(*medians)
    print(*mods)
    print(med(medians), '\n' + mod(mods))
    print(med(all_numbers), '\n' + mod(all_numbers))


def med(list_):
    list_.sort()
    return list_[len(list_) // 2]


def mod(list_):
    return max(list_, key=list_.count)


f()
