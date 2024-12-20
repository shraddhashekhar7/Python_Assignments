def calc_sum_odd(s,e):
    sum_odd = 0
    for number in range(s, e + 1):
        if number % 2 != 0:
            sum_odd += number
    print("Sum of odd numbers is: ", sum_odd)


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
calc_sum_odd(start, end)