def longest_consecutive_sequence(arr):
    if not arr:
        return 0
    arr.sort()
    print(arr)
    current_length = 1
    list=[]
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_length += 1
        elif arr[i] != arr[i - 1]+1:
            list.append(current_length)
            current_length = 1
    return list
arr1 = list(map(int, input().split()))
result1 = longest_consecutive_sequence(arr1)
print(result1)