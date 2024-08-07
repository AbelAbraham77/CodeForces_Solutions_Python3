def can_shower():
    t = int(input())
    results = []

    for i in range(t):
        n, s, m = map(int, input().split())
        intervals = []
        
        for i in range(n):
            l, r = map(int, input().split())
            intervals.append((l, r))
        
        intervals.sort()
        
        can_shower = False
        
        if intervals[0][0] >= s:
            can_shower = True
        
        for i in range(1, n):
            if intervals[i][0] - intervals[i-1][1] >= s:
                can_shower = True
        
        if m - intervals[-1][1] >= s:
            can_shower = True
        
        if can_shower:
            results.append("YES")
        else:
            results.append("NO")
    
    for result in results:
        print(result)

can_shower()
