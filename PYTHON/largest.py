def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr =[]
a=int(input("Enter first Number:"))
arr.append(a)
b=int(input("Enter second number:"))
arr.append(b)
c=int(input("Enter third number:"))
arr.append(c)
bubbleSort(arr)
print(arr[1])