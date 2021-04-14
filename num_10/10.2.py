def cesar():
    step, word = int(input()), input()
    result, sigh = [], [' ', ',', '.', '?', '!']
    for letter in word:
        if letter not in sigh:
            result.append(chr(ord(letter) + step))
        else:
            result.append(letter)
    print(*result, sep="")


cesar()
