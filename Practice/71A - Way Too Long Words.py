def word_abb():
    n = int(input())
    updated_list = []

    for i in range (0, n):
        word = input()
        if len(word)>10:
            word = word[0] + str(len(word) - 2) + word[-1]
        updated_list.append(word)
    
    for item in updated_list:
        print(item)

word_abb()