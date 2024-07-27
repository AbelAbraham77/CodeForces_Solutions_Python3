def countlegs(n: int):
    count = 0
    if n<2 or n == 3:
        return
    if n%4==0:
        return (int(n/4))
    elif n%4!=0:
        count = int(n/4)
        remaining = n - (int((n/4))*4)
        count += remaining/2

        return (int(count))

n1 = int(input())

list1 = []
for i in range (0, n1):
    num = int(input())
    list1.append(countlegs(num))

for item in list1:
    print(item)