def cp_points():
    n = int(input())
    total_points = 0

    for i in range(0, n):
        data = input()
        useful_data = data.split()
        problem_points = 0
        for item in useful_data:
            problem_points += int(item)
        if problem_points >= 2:
            total_points +=1
    
    print(total_points)

cp_points()