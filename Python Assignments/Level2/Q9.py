my_list = [10, 20, 30, 40, 50]

def handle_error(index):
    try:
        print(f"Element at index {index}: {my_list[index]}")
    except IndexError:
        print(f"Error: Index {index} is out of range.")

handle_error(2)
handle_error(5)
