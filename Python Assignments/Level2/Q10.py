def stone_piles(n):
    piles = []
    i = 1 if n % 2 != 0 else 2

    while i < n:
        piles.append(i)
        i += 2

    return piles


n = 7
result = stone_piles(n)
print(f"Stones in a single pile = {result}")
