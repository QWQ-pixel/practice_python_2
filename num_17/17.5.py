def access():
    num = int(input())
    if 1 <= num <= 100:
        access_list = [input() for _ in range(num)]
        num = int(input())
        if 1 <= num <= 100:
            request_list = [input() for _ in range(num)]
            for acc in access_list:
                for req in request_list:
                    if req.startswith(acc):
                        print('YES')
                        break
                    else:
                        print('NO')
                        break


access()
