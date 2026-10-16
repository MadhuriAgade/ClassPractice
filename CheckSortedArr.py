# def isArraySorted(n, arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
#     return True
# arr = [3,1,6,9]
# print(isArraySorted(len(arr),arr))

def isArraySorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
arr = [1,2,3,4]  
print(isArraySorted(arr))  