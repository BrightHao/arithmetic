a, b, c, d, e, f, g = [int(i) for i in input().split()]

if d <= c:
    print(g*d)
elif d <= b+c:
    print(g*c+f*(d-c))
elif d <= a+b+c:
    print(g*c+f*b+e*(d-b-c))
else:
    print(g*c+f*b+e*a)
