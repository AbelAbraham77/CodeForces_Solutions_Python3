def move_on(n, k, scores):
    k_score = scores[k-1]
    
    advancing_count = 0
    for score in scores:
        if score >= k_score and score > 0:
            advancing_count += 1
            
    return advancing_count

n, k = map(int, input().split())
scores = list(map(int, input().split()))

result = move_on(n, k, scores)

print(result)

    