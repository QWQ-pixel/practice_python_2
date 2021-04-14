def game():
    num, stuff = int(input()), []
    for i in range(num):
        stuff.append(input())
    k = int(input())
    for i in range(k):
        x, empty_stuff = int(input()), []
        for j in range(x):
            empty_stuff.append(stuff[int(input()) - 1])
        stuff = empty_stuff
    for s in stuff:
        print(s)


game()
