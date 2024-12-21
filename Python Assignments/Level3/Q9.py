def encode(inputstr):
    res = ""
    i = 0
    while i < len(inputstr):
        ch = inputstr[i]
        count = 0
        while i < len(inputstr) and inputstr[i] == ch:
            count += 1
            i += 1
        res += ch + str(count)
    return res


inputstr = "wwwwaaadebbbbbw"
print(encode(inputstr))
