def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)

    except FileNotFoundError:
        return "The file does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "demo.txt"
print("There are {} lines.".format(count_lines(file_path)))