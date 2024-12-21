def get_even_len(file_path):
    try:
        with open(file_path, 'r') as file:
            result = []
            for line in file:
                words = line.strip().split()
                even_len_words = [word for word in words if len(word) % 2 == 0]
                result.append(" ".join(even_len_words))
            return " ".join(result)

    except FileNotFoundError:
        return "The file does not exist."
    except Exception as e:
        return f"An error occurred: {e}"


file_path = "doc.txt"
print(get_even_len(file_path))