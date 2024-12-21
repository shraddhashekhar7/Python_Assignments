def JtoI(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            correct = content.replace('J', 'I')
            correct = correct.replace('j', 'i')
            return correct

    except FileNotFoundError:
        return "The file does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "words.txt"
print(JtoI(file_path))