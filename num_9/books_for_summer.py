
def summer_books():
    num_lib, num_sum = int(input()), int(input())
    library, summer_list = input_books(num_lib), input_books(num_sum)
    for book in summer_list:
        if book in library:
            print("YES")
        else:
            print("NO")


def input_books(num):
    books = list()
    for i in range(num):
        book = input()
        books.append(book)
    return books


summer_books()


