def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


list1 = [1, 2, 2, 3, 4, 4, 5, 5]

list2 = unique_elements(list1)
print(f"List with unique elements: {list2}")