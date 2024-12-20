def reverse_sent(sent):
    rev_sent = sent.split()[::-1]
    print(" ".join(rev_sent))


input_sentence = "Hello, World! Welcome to Python programming."
reverse_sent(input_sentence)