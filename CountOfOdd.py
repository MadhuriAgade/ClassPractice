def countOdd(n, arr):
    count = 0
    for i in range(n):
        if arr[i] % 2 == 1:
            count += 1
    return count      
arr = [2,4,6,1,7]
print(countOdd(len(arr), arr))