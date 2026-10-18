def secondHighestOccurring(arr):
    counts = []

    for i in arr:
        counts.append(arr.count(i))

    first = max(counts)
    second = 0
    ans = arr[0]

    for i in arr:
        count = arr.count(i)

        if count < first and count > second:
            second = count
            ans = i
        elif count == second and i < ans:
            ans = i

    return ans