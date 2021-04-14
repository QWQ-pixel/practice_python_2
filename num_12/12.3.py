def list_prod():
    num, prod, list_ = int(input()), dict(), list()
    for i in range(num):
        product = input()
        prod[product] = int(input())
    for key, value in prod.items():
        list_.append("{0} {1}".format(key, value))
    list_.reverse()
    print(*list_, sep='\n')


list_prod()
