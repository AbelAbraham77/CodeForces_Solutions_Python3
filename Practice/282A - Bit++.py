def calc_bit():
    n = int(input())
    value_x = 0

    for i in range(0, n):
        op_x = input()
        if "+" in op_x:
            value_x += 1
        elif "-" in op_x:
            value_x -= 1
    
    print(value_x)

calc_bit()