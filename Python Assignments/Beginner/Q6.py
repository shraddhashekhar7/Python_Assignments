def perfect(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        print("Yes")
    else:
        print("No")


num = int(input("Enter a number: "))
perfect(num)
