def calculate_typing_time(s):
    if not s:
        return 0
    time = 2  # time for the first character
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            time += 1
        else:
            time += 2
    return time

def strong_pass():
    import string
    
    results = []
    test_cases = []

    n = int(input())
    for i in range(n):
        text = input()
        test_cases.append(text)
    for s in test_cases:
        max_time = 0
        best_string = s
        for i in range(len(s) + 1):
            for c in string.ascii_lowercase:
                new_string = s[:i] + c + s[i:]
                typing_time = calculate_typing_time(new_string)
                if typing_time > max_time:
                    max_time = typing_time
                    best_string = new_string
        results.append(best_string)
        
    for i in results:
        print(i)

strong_pass()