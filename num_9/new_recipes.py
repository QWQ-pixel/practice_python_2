def new_rec():
    num_rec, all_rec, use_rec = int(input()), list(), dict()
    for i in range(num_rec):
        all_rec.append(input())
    num_days = int(input())
    for rec in all_rec:
        use_rec[rec] = 0
    for i in range(num_days):
        num_rec_in_day = int(input())
        for j in range(num_rec_in_day):
            recipe = input()
            if recipe in all_rec:
                use_rec[recipe] = 1
    for key in use_rec.keys():
        if use_rec.get(key) == 0:
            print(key)


new_rec()

