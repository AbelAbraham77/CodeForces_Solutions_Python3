def count_suneet_wins(a1, a2, b1, b2):
    from itertools import permutations
    
    suneet_cards = [a1, a2]
    slavic_cards = [b1, b2]
    
    win_count = 0
    
    for suneet_perm in permutations(suneet_cards):
        for slavic_perm in permutations(slavic_cards):
            suneet_wins = 0
            slavic_wins = 0
            
            if suneet_perm[0] > slavic_perm[0]:
                suneet_wins += 1
            elif suneet_perm[0] < slavic_perm[0]:
                slavic_wins += 1
            
            if suneet_perm[1] > slavic_perm[1]:
                suneet_wins += 1
            elif suneet_perm[1] < slavic_perm[1]:
                slavic_wins += 1
            
            if suneet_wins > slavic_wins:
                win_count += 1
    
    return win_count

def solve(test_cases):
    results = []
    for a1, a2, b1, b2 in test_cases:
        results.append(count_suneet_wins(a1, a2, b1, b2))
    
    for result in results:
        print(result)

t = int(input())
test_cases = []
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    test_cases.append((a1, a2, b1, b2))

solve(test_cases)
