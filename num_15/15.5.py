def f():
    nums, queue = int(input()), []
    for i in range(nums):
        s = input().split()
        if 'встал' in s[1]:
            queue.append(s[0])
        elif s[0] == 'Привет,':
            queue.insert(queue.index(s[1][:-1]) + 1, s[2])
        elif s[1] == 'хватит':
            queue.remove(s[0][:-1])
    print(*queue, sep='\n')


f()
