def calculate_lcm(a, b):
    lcm = max(a, b)
    while True:
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        lcm += 1


number1 = int(input("Enter num 1: "))
number2 = int(input("Enter num 2: "))

lcm = calculate_lcm(number1, number2)
print(f"LCM of {number1} and {number2} is: {lcm}")