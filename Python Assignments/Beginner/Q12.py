def reverse_number(num):
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num


num = int(input("Enter a number: "))

revnum = reverse_number(num)
print("Reversed number: ",revnum)