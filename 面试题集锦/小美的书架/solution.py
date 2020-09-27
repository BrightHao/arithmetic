N, M, Q = [int(i) for i in input().split()]

yy = {}  # 行
xx = {}  # 书编号

for i in range(M):
    # 1表示没锁
    yy[i] = 1


for i in range(Q):
    t = input()
    if t[0] == '1':
        x, y, z = [int(i) for i in t.split()]
        xx[y] = z
    else:
        n, o = [int(i) for i in t.split()]
        if n == 2:
            yy[o] = 0
        if n == 3:
            yy[o] = 1
        if n == 4:
            if o in xx and yy[xx[o]]:
                print(xx[o])
            else:
                print(-1)
