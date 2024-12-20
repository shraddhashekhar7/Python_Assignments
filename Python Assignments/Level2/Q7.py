def find_median(number_list):
    number_list.sort()
    n = len(number_list)

    if n % 2 == 1:
        median = number_list[n // 2]
    else:
        m = n // 2
        m1 = number_list[m - 1]
        m2 = number_list[m]
        median = (m1 + m2) / 2

    return median


number_list = [7, 2, 5, 1, 9, 3]
median = find_median(number_list)
print(f"Median: {median}")
