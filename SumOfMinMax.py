def sumHighestLowest(arr):
    max_count = 0
    min_count = len(arr)

    for i in arr:
        count = arr.count(i)

        if count > max_count:
            max_count = count

        if count < min_count:
            min_count = count

    return max_count + min_count