from statistics import mean


def wh(num_prt):
    list_prt = dict()
    for i in range(num_prt):
        name = input()
        list_prt[name] = int(input())
    mean_num = mean(list_prt.values())
    list_ = list(list_prt.keys())
    for key in list_prt.keys():
        if list_prt[key] > mean_num:
            print(key)
            list_.remove(key)
    print(*sorted(list_), sep="\n")


if __name__ == "__main__":
    num = int(input())
    if num > 0:
        wh(num)
