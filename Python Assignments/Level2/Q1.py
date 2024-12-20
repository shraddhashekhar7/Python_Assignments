def common_elements(l1, l2):
    common = []
    for element in l1:
        if element in l2 and element not in common:
            common.append(element)
    return common


l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

result = common_elements(l1, l2)
print("Common elements: ",result)