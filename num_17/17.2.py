def phone_numbers():
    num, phone = int(input()), dict()
    if 1 <= num <= 100:
        for i in range(num):
            string = input().split()
            if string[-1] in phone.keys():
                phone[string[-1]] += ' ' + string[0]
            else:
                phone[string[-1]] = string[0]
        num = int(input())
        list_ = [input() for _ in range(num)]
        for name in list_:
            if name in phone.keys():
                print(phone[name])
            else:
                print('Нет в телефонной книге')


phone_numbers()
