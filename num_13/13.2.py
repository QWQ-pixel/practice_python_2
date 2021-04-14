def rev(num):
    numbers = []
    for i in range(num):
        numbers.append(int(input()))
    print(*sorted(numbers, reverse=True), sep="\n")


if __name__ == "__main__":
    n = int(input())
    rev(n)
