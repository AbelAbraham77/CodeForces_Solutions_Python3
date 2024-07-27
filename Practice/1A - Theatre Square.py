import math 

def theatresquare(n, m, a):
    square_length = math.ceil(n/a)

    square_width = math.ceil(m/a)

    print(square_length*square_width)

data = input()
useful_data = data.split()
n = int(useful_data[0])
m = int(useful_data[1])
a = int(useful_data[2])

theatresquare(n, m, a)