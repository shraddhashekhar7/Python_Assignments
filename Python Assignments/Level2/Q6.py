def is_power_of_two(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)


number = int(input("Enter a number: "))
if is_power_of_two(number):
    print(f"{number} is a power of two.")
else:
    print(f"{number} is not a power of two.")
