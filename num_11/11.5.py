def eat_letters(string):
    if string:
        print(string)
        return eat_letters(string[1:-1])


eat_letters(input())
