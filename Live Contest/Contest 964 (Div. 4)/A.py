def sumdigits():
    n = int(input())
    results = []
    for i in range(n):
        num = int(input())
        digits = [int(a) for a in str(num)]
        sum = 0
        for digit in digits:
            sum += digit
        results.append(sum)
    
    for result in results:
        print(result)

sumdigits()