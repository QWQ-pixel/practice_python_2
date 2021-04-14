def f():
    let, string = input(), input()
    sep_string = string.split()
    for i in sep_string:
        if let in i.lower():
            print(i)


f()
