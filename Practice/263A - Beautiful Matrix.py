def beautiful_matrix():
    matrix_rows = []
    for i in range(0,5):
        row = input()
        row_list = row.split()
        matrix_rows.append(row_list)
    
    if matrix_rows[2][2] == "1":
        print(0)
    else:
        if "1" in [matrix_rows[0][0], matrix_rows[4][4], matrix_rows[4][0], matrix_rows[0][4]]:
            print(4)
        elif "1" in [matrix_rows[0][1], matrix_rows[0][3], matrix_rows[1][0], matrix_rows[1][4], matrix_rows[3][0], matrix_rows[3][4], matrix_rows[4][1], matrix_rows[4][3]]:
            print(3)
        elif "1" in [matrix_rows[0][2], matrix_rows[1][1], matrix_rows[1][3], matrix_rows[2][0], matrix_rows[2][4], matrix_rows[3][1], matrix_rows[3][3], matrix_rows[4][2]]:
            print(2)
        elif "1" in [matrix_rows[1][2], matrix_rows[2][1], matrix_rows[2][3], matrix_rows[3][2]]:
            print(1)
    

beautiful_matrix()
