def min_operations_to_same_parity(t, test_cases):
    results = []
    for n, a in test_cases:
        even_count = sum(1 for x in a if x % 2 == 0)
        odd_count = n - even_count  # Since all are either even or odd
        # The minimum operations needed to make all elements have the same parity
        results.append(min(even_count, odd_count))
    return results


n = int(input())
for i in range(n):
    num_testcases = int(input())
    data = input().split()
    test_cases.append([num_testcases, data])
index = 0
t = int(data[index])
index += 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    test_cases.append((n, a))

# Get results
results = min_operations_to_same_parity(t, test_cases)

# Print results
for result in results:
    print(result)
