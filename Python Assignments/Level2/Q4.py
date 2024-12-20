def rotate_array(arr, D):
    for i in range(D):
        arr.insert(0, arr.pop())

    return arr


input_list = [1,2,3,4,5]
D = 2
print(rotate_array(input_list, D))
