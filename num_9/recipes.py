def recipes():
    num, products, recipe = int(input()), list(), dict()
    for i in range(num):
        products.append(input())
    num = int(input())
    for i in range(num):
        name, num_prod, list_ = input(), int(input()), list()
        for j in range(num_prod):
            ingredient = input()
            if ingredient in products:
                flag = True
            else:
                flag = False
            list_.append(ingredient)
            if j == num_prod - 1:
                list_.append(flag)
        recipe[name] = list_
    for k in recipe.keys():
        if recipe.get(k)[-1]:
            print(k)


recipes()
