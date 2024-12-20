def count_frequency(input_list):
    frequency = {}
    for item in input_list:
        frequency[item] = frequency.get(item, 0) + 1

    return frequency


input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
result = count_frequency(input_list)

print("Frequency count:", result)