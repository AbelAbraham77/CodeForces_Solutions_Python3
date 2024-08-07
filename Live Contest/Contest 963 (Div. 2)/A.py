def max_correct_answers(t, test_cases):
    results = []

    for case in test_cases:
        n, s = case
        count_A = s.count('A')
        count_B = s.count('B')
        count_C = s.count('C')
        count_D = s.count('D')
        count_q = s.count('?')

        # Calculate how many of each answer are needed to reach exactly n
        needed_A = max(0, n - count_A)
        needed_B = max(0, n - count_B)
        needed_C = max(0, n - count_C)
        needed_D = max(0, n - count_D)

        total_needed = needed_A + needed_B + needed_C + needed_D

        # Calculate the maximum score Tim can achieve
        if total_needed <= count_q:
            max_score = count_A + count_B + count_C + count_D + total_needed
        else:
            # Not enough '?' to fill all gaps, so only already correct answers are counted
            max_score = count_A + count_B + count_C + count_D

        results.append(min(max_score, 4 * n))
    return results

# Main program
num_testcases = int(input())
test_cases = []

for _ in range(num_testcases):
    num_ans = int(input())
    answers = input().strip()
    test_cases.append((num_ans, answers))

results = max_correct_answers(num_testcases, test_cases)
for result in results:
    print(result)
