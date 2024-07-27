
def reducebyfactor(n, k, grid):
    r_grid = []
    for i in range(0, n, k):
        r_row = []
        for j in range(0, n, k):
            r_row.append(grid[i][j])
        r_grid.append(''.join(r_row))
    return r_grid


num_iterations = int(input())

results = []
for i in range(num_iterations):
    n, k = map(int, input().split())
    grid = [input().strip() for i in range(n)]
    reduced_grid = reducebyfactor(n, k, grid)
    results.append(reduced_grid)

for result in results:
    for row in result:
        print(row)
