def can_form_subsequence(s, t):
    it = iter(s)
    return all(char in it for char in t)

def solve(test_cases):
    results = []
    for s, t in test_cases:
        t_len = len(t)
        new_s = list(s)
        
        s_ptr, t_ptr = 0, 0
        while s_ptr < len(new_s) and t_ptr < t_len:
            if new_s[s_ptr] == '?':
                new_s[s_ptr] = t[t_ptr]
                t_ptr += 1
            elif new_s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            s_ptr += 1
        
        new_s = [char if char != '?' else 'a' for char in new_s]

        if can_form_subsequence(new_s, t):
            results.append("YES")
            results.append("".join(new_s))
        else:
            results.append("NO")
    
    for result in results:
        print(result)

n = int(input())
test_cases = []

for _ in range(n):
    str1 = input().strip()
    str2 = input().strip()
    test_cases.append((str1, str2))

solve(test_cases)

