def clear():
    num, white_list = int(input()), []
    for i in range(num):
        white_list.append(input())
    num, search_list = int(input()), []
    for i in range(num):
        search_list.append(input())
    print(*set(white_list) & set(search_list), sep='\n')


clear()
