def two_ways(num_):
    list_br1, list_br2 = [], []
    for i in range(num_):
        count = int(input())
        list_br1.append(count)
        list_br2.append(count)
    num_workouts = int(input())
    for i in range(num_workouts):
        br = int(input())
        if br == 1:
            list_br1 = skill(list_br1)
        elif br == 2:
            list_br2 = skill(list_br2)
    print(*list_br1, "\n", *list_br2, "\n", len(set(list_br1) & set(list_br2)))


def skill(list_):
    index = int(input())
    if index < len(list_):
        num_ = int(input())
        list_[index] += num_
    return list_


if __name__ == "__main__":
    number_skill = int(input())
    if number_skill > 0:
        two_ways(number_skill)
