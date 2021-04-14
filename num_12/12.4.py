def rle():
    string, count = input(), 0
    if len(string) == 1:
        print(1, string)
    else:
        for i in range(len(string)):
            if i <= len(string):
                if i == len(string)-1:
                    print(count, string[i])
                    break
                if string[i] == string[i + 1]:
                    count += 1
                else:
                    print(count, string[i])
                    count = 1


rle()
