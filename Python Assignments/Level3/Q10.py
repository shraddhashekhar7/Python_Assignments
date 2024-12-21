def return_customer(N, S):
    taken = set()
    ret_cust = 0
    returned = set()
    for i in S:
        if i in taken:
            taken.remove(i)
        elif i not in taken and i not in returned and len(taken) < N:
            taken.add(i)
        elif i not in returned:
            returned.add(i)
            ret_cust += 1
    return ret_cust


N = 3
S = "GACCBDDBAGEE"
print(return_customer(N, S))