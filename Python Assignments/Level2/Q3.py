def count_pairs(arr, k):
    seen = set()
    count = 0

    for num in arr:
        complement = k - num
        if complement in seen:
            count += 1

        seen.add(num)

    return count


arr = [1, 2, 3, 4, 5]
k = 6

pair_count = count_pairs(arr, k)
print(f"Pair count: {pair_count}")