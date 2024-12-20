def anagrams(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    return sorted(string1) == sorted(string2)


string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

print(anagrams(string1, string2))

