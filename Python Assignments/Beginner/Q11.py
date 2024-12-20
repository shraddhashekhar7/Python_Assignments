def sum_digits(num):
    while num >= 10:
        inter_sum = 0
        for digit in str(num):
            inter_sum += int(digit)
        num = inter_sum
    return num


num = int(input("Enter a number: "))

final_result = sum_digits(num)
print("Final Output: ",final_result)