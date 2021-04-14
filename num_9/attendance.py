def attendance():
    num_list = int(input())
    all_lists, students = list(), set()
    for i in range(num_list):
        all_lists.append(students_list())
    for i in range(1, len(all_lists)):
        if i == 1:
            students = set(all_lists[0]) & set(all_lists[i])
        else:
            students = set(students) & set(all_lists[i])
    print(students)


def print_list(list_):
    for items in list_:
        print(items)


def students_list():
    num = int(input())
    students = list()
    for j in range(num):
        student = input()
        students.append(student)
    return students


attendance()
