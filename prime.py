def f_1():
    for i in range(904528, 997438+1):
        s = set()
        for j in range(1, int(i ** 0.5)+1):
            if i % j == 0:
                s.add(j)
                s.add(i // j)
            if len(s) > 5:
                break
        # print(s)
        if len(s) == 5:
            print(*sorted(list(s)))


def f_2():
    mx = [0, 0, 0, []]
    for i in range(268220, 270335+1):
        s = set()
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                s.add(j)
                s.add(i // j)
            if len(s) > 4:
                break
        if len(s) <= 4:
            if mx[1] <= sum(s):
                mx[0] = i
                mx[1] = sum(s)
                mx[2] = len(s)
                mx[3] = sorted(s, reverse=True)
    print(*mx)


def f_3():
    c = 0
    for i in range(2484292,2484370+1):

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            c += 1
            print(c, i)


for i in '123':
    eval('f_' + i)()
