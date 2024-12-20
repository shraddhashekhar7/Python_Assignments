def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count


string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"Number of vowels: {vowel_count}")
