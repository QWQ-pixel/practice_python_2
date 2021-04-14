
def fraction():
    num, num_, list_1, list_2 = int(input()), 1, [], []
    while num_ not in list_1:
        list_1.append(num_)
        list_2.append(10 * num_ // num)
        num_ = 10 * num_ % num
    print(*list_2[list_1.index(num_):], sep='')


fraction()
