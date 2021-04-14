def f():
    string, key = input(), input()
    string = string.replace('?', ' ').replace('=', ' ').replace('&', ' ')
    sep_string, sep_dict = string.split(), dict()
    for i in sep_string[1:]:
        if sep_string.index(i) % 2 != 0:
            sep_dict[i] = sep_string[sep_string.index(i)+1]
    if key in sep_dict.keys():
        print(sep_dict[key])


f()
