def max_dominoes():
    m, n = map(int, input().split())
    rectangle_area = m*n
    max_d = int(rectangle_area/2)

    print(max_d)

max_dominoes()