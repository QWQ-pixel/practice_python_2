def bacteria():
    num, bacteria_cell, list_ = int(input()), [], []
    if num >= 3:
        for i in range(num):
            for j in range(num):
                list_.append(int(input()))
            bacteria_cell.append(list_)
            list_ = []
        for _ in range(int(input())):
            x = int(input())
            y = int(input())
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i <= len(bacteria_cell) - 1 and 0 <= y + j <= len(bacteria_cell)-1:
                        bacteria_cell[x + i][y + j] -= 8 if i == 0 and j == 0 else 4
                        if bacteria_cell[x + i][y + j] < 0:
                            bacteria_cell[x + i][y + j] = 0
    print(*bacteria_cell, sep='\n')


bacteria()
