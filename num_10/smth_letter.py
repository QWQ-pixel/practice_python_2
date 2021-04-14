def letters():
    word, num = input(), int(input())
    if len(word) >= num > 0:
        print(word[num - 1])
    else:
        print("ОШИБКА")


letters()
