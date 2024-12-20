def count_alpha_num(s):
    alpha, num = 0, 0
    for ch in s:
        if ch.isalpha():
            alpha += 1
        elif ch.isdigit():
            num += 1
    print("Alphabets: ", alpha, " Numbers: ", num)

inputStr = input("Enter the string: ")
count_alpha_num(inputStr)
