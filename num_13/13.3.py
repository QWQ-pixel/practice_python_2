def sequence(n):
    seq = []
    for i in range(n):
        a = 0
        for j in range(i):
            if seq[j] == seq[-j - 1]:
                a += 1
        seq.append(a)
        print(a)


if __name__ == "__main__":
    num = int(input())
    sequence(num)
