def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2


data = [-200,-3,89,0,1,45,-67,54]
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)